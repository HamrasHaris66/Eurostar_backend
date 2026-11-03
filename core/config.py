from functools import lru_cache
from pathlib import Path
from typing import Self

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


APP_ROOT = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(APP_ROOT / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Which upstream environment to hit
    ACTIVE_ENV: str = "TEST"  # TEST | PROD

    # Sandbox credentials
    TEST_BASE_URL: str = "https://sandbox.eurostar.com"
    TEST_X_API_KEY: str = ""

    # Production credentials
    PROD_BASE_URL: str = ""
    PROD_X_API_KEY: str = ""

    # Incoming auth for this sub-app (comma-separated)
    API_KEYS: str = ""

    @property
    def is_production(self) -> bool:
        return self.ACTIVE_ENV.upper() == "PROD"

    @property
    def base_url(self) -> str:
        return self.PROD_BASE_URL if self.is_production else self.TEST_BASE_URL

    @property
    def x_api_key(self) -> str:
        return self.PROD_X_API_KEY if self.is_production else self.TEST_X_API_KEY

    @model_validator(mode="after")
    def _check_active_credentials(self) -> Self:
        if self.is_production:
            if not self.PROD_X_API_KEY:
                raise ValueError("PROD_X_API_KEY is required when ACTIVE_ENV=PROD")
            if not self.PROD_BASE_URL:
                raise ValueError("PROD_BASE_URL is required when ACTIVE_ENV=PROD")
        else:
            if not self.TEST_X_API_KEY:
                raise ValueError("TEST_X_API_KEY is required when ACTIVE_ENV=TEST")
        if not self.API_KEYS:
            raise ValueError("API_KEYS is required (comma-separated)")
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()



EUROSTAR_MARKET = "GB"
EUROSTAR_USER_AGENT = "eurostar-app"