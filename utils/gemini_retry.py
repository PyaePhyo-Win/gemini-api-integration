from __future__ import annotations

from typing import Any

from tenacity import RetryCallState, retry, retry_if_exception_type, stop_after_attempt, wait_exponential


class RateLimitError(Exception):
    """Raised when Gemini hits a retryable rate limit or quota error."""


def is_rate_limit_error(error: Exception) -> bool:
    message = str(error).upper()
    return (
        "429" in message
        or "RESOURCE_EXHAUSTED" in message
        or "RATE LIMIT" in message
        or "RATE_LIMIT" in message
        or "QUOTA" in message
    )


def generate_content_with_retry(
    *,
    client: Any,
    model: str,
    contents: Any,
    config: Any | None = None,
    max_attempts: int = 5,
    min_wait: int = 2,
    max_wait: int = 10,
    **kwargs: Any,
) -> Any:
    """Call Gemini with retry handling for transient rate-limit failures."""

    def log_retry(retry_state: RetryCallState) -> None:
        sleep_seconds = retry_state.next_action.sleep if retry_state.next_action else 0
        print(
            "Gemini rate limit hit. "
            f"Retrying in {sleep_seconds:.1f}s "
            f"(attempt {retry_state.attempt_number + 1}/{max_attempts})"
        )

    @retry(
        wait=wait_exponential(multiplier=1, min=min_wait, max=max_wait),
        stop=stop_after_attempt(max_attempts),
        retry=retry_if_exception_type(RateLimitError),
        before_sleep=log_retry,
        reraise=True,
    )
    def run_request() -> Any:
        try:
            return client.models.generate_content(
                model=model,
                contents=contents,
                config=config,
                **kwargs,
            )
        except Exception as error:
            if is_rate_limit_error(error):
                raise RateLimitError(str(error)) from error
            raise

    return run_request()
