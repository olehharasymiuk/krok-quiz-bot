from .throttling import ThrottlingMiddleware


def setup_middleware(dp):
    dp.middleware.setup(ThrottlingMiddleware())
