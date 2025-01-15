from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_prefix='DB_', extra='ignore')
    HOST: str = ''
    PORT: int = 0
    NAME: str = ''
    PASSWD: str = ''
    NAME: str = ''

    def get_prod_link(self):
        return f"postgresql+asyncpg://{
            self.user}:{
            self.passwd}@{
            self.host}:{
                self.port}/{
                    self.name}?async_fallback=True"

    def get_test_link(self):
        return 'sqlite+aiosqlite:///:memory:'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()

if __name__ == '__main__':
    print(Settings().model_dump())