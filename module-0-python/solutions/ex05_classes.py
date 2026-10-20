from dataclasses import dataclass


@dataclass
class TokenBudget:
    limit: int
    used: int = 0

    @property
    def remaining(self) -> int:
        return self.limit - self.used

    def spend(self, tokens: int) -> int:
        if tokens < 0:
            raise ValueError("tokens must be >= 0")
        if tokens > self.remaining:
            raise ValueError("budget exceeded")
        self.used += tokens
        return self.remaining
