from fastapi import HTTPException


BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "developer message",
    "forget previous",
    "bypass",
    "jailbreak"
]


def validate_request(request: str) -> str:
    """
    Validates incoming user requests.
    """

    request = request.strip()

    if not request:
        raise HTTPException(
            status_code=400,
            detail="Request cannot be empty."
        )

    if len(request) < 10:
        raise HTTPException(
            status_code=400,
            detail="Request must contain at least 10 characters."
        )

    if len(request) > 3000:
        raise HTTPException(
            status_code=400,
            detail="Request is too large."
        )

    lower_request = request.lower()

    for pattern in BLOCKED_PATTERNS:

        if pattern in lower_request:

            raise HTTPException(
                status_code=400,
                detail="Unsafe prompt detected."
            )

    return request