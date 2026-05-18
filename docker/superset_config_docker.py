import os


FEATURE_FLAGS = {
    # Новые для v6
    "DASHBOARD_RBAC": True,
    "DRILL_BY": True,  
    "DRILL_TO_DETAIL": True,
    # "GLOBAL_ASYNC_QUERIES": True, 
    "ENABLE_SUPERSET_META_DB": True,
    "TAGGING_SYSTEM": True,
    "ENABLE_UI_THEME_ADMINISTRATION": True,
    "AG_GRID_TABLE_ENABLED": True,
    # Перенесено с v2
    "ALERT_REPORTS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "GENERIC_CHART_AXES": True,
    "THUMBNAILS_SQLA_LISTENERS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_CACHE": True,
    "ENABLE_JAVASCRIPT_CONTROLS": True,
    "EMBEDDABLE_CHARTS": True,
    "ALLOW_ADHOC_SUBQUERY": True
}



THEME_DEFAULT = {"token": {"brandAppName": "Superset", "brandLogoAlt": "Apache Superset", 
"brandLogoUrl": "/static/assets/images/superset-logo-horiz.png", 
"brandLogoMargin": "0 -10px 0 0",
"brandLogoHref": "/", "brandLogoHeight": "42px",
"colorPrimary": "#2893B3", "colorLink": "#2893B3", "colorError": "#e04355", "colorWarning": "#fcc700", 
"colorSuccess": "#5ac189", "colorInfo": "#66bcfe", "fontUrls": [], "fontFamily": "Inter, Helvetica, Arial, sans-serif", 
"fontFamilyCode": "'IBM Plex Mono', 'Courier New', monospace", "transitionTiming": 0.3, "brandIconMaxWidth": 37, 
"fontSizeXS": "8", "fontSizeXXL": "28", "fontWeightNormal": "400", "fontWeightLight": "300", 
"fontWeightStrong": "500", "fontWeightBold": "700", "colorEditorSelection": "#fff5cf"}, "algorithm": "default"}

THEME_DARK = {"token": {"brandAppName": "Superset", "brandLogoAlt": "Apache Superset",
"brandLogoUrl": "/static/assets/images/superset-logo-horiz.png", 
"brandLogoMargin": "0 -10px 0 0",
"brandLogoHref": "/", "brandLogoHeight": "42px",
"colorPrimary": "#2893B3", "colorLink": "#2893B3", "colorError": "#e04355", "colorWarning": "#fcc700", 
"colorSuccess": "#5ac189", "colorInfo": "#66bcfe", "fontUrls": [], "fontFamily": "Inter, Helvetica, Arial, sans-serif", 
"fontFamilyCode": "'IBM Plex Mono', 'Courier New', monospace", "transitionTiming": 0.3, "brandIconMaxWidth": 37, 
"fontSizeXS": "8", "fontSizeXXL": "28", "fontWeightNormal": "400", "fontWeightLight": "300", 
"fontWeightStrong": "500", "fontWeightBold": "700", "colorEditorSelection": "#5c4d1a"}, "algorithm": "dark"}

PUBLIC_ROLE_LIKE_GAMMA = True

# BUILD_NUMBER = "Dlake 1.0.0"
SUPERSET_DASHBOARD_POSITION_DATA_LIMIT = 531070
# To avoid default key warning
SECRET_KEY = 'IbAS6GQqzfyKhcPjMom7gHRT1OrBCV02xd5kas9Ev4FpZlUutY'

os.environ['SUPERSET_ENV'] = 'production'
os.environ['FLASK_ENV'] = 'production'

# Альтернативный способ, если прямое указание через os.environ не помогло
SUPERSET_ENV = 'production'
FLASK_ENV = 'production'

# Translation config
BABEL_DEFAULT_LOCALE = "ru"
BABEL_DEFAULT_FOLDER = "superset/translations"
LANGUAGES = {
    "en": {"flag":"us", "name": "English"},
    "ru": {"flag":"ru","name": "Russian"}
}

# from superset.translations.utils import get_language_pack

# def override_bootstrap_locale(data):
#     if data.get("locale") == "ru":
#         data["locale"] = "ru_RU"
#         data["language_pack"] = get_language_pack("ru_RU")
#     return data


# COMMON_BOOTSTRAP_OVERRIDES_FUNC = override_bootstrap_locale



CSV_EXPORT = {"encoding": "cp1251", "sep": ";"}

ENABLE_TIME_ROTATE = False # use for superset logging

SQL_MAX_ROW = 200000


SESSION_COOKIE_SAMESITE = None
CONTENT_SECURITY_POLICY_WARNING= False

HTML_SANITIZATION = True
HTML_SANITIZATION_SCHEMA_EXTENSIONS = {
  "attributes": {
    "*": ["style","className"],
  },
  "tagNames": ["style"],
}

EXTRA_CATEGORICAL_COLOR_SCHEMES = [
    {
        "id": 'GDscheme',
        "description": '',
        "label": 'GD color scheme',
        "isDefault": False,
        "colors": ['#7978E9', '#98BDFF', '#74A67E', '#CFE0AD', '#FFA95A', '#F7CC7F', '#F3797E', '#EB9995']
    }
]


#  Async queries
# GLOBAL_ASYNC_QUERIES_JWT_SECRET = "xK8fR9tG2hJ7kL3mN5pQ6rS9uV1wX4yZ7bC0eF3="

# REDIS_HOST = os.getenv("REDIS_HOST", "redis")
# REDIS_PORT = os.getenv("REDIS_PORT", "6379")
# REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
# REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

# GLOBAL_ASYNC_QUERIES_CACHE_BACKEND = {
#     "CACHE_TYPE": "RedisCache",
#     "CACHE_DEFAULT_TIMEOUT": 60*60*24,
#     "CACHE_KEY_PREFIX": "superset_async_",
#     "CACHE_REDIS_HOST": REDIS_HOST,
#     "CACHE_REDIS_PORT": REDIS_PORT,
#     "CACHE_REDIS_DB": REDIS_RESULTS_DB
# }

# GLOBAL_ASYNC_QUERIES_REDIS_CONFIG = {
#     "host": REDIS_HOST,
#     "port": REDIS_PORT,
#     "db": REDIS_RESULTS_DB
# }

DECKGL_BASE_MAP = [
    ['tile://https://core-sat.maps.yandex.net/tiles?l=sat&v=1.11.30&x={x}&y={y}&z={z}&scale=1&lang=ru_RU', 'YandexMap Спутник'],
    ['tile://https://core-renderer-tiles.maps.yandex.net/tiles?l=map&v=21.02.16-0&x={x}&y={y}&z={z}&scale=1&lang=ru_RU', 'YandexMap схема']

]

ENABLE_CORS = True

CORS_OPTIONS = {
    "origins": [
        "https://core-sat.maps.yandex.net",  # Яндекс тайлы
  "https://core-renderer-tiles.maps.yandex.net"
    ]
}

TALISMAN_CONFIG = {
    "content_security_policy": {
        "connect-src": [
            "'self'",
            "https://core-sat.maps.yandex.net",  # Яндекс подложка
      "https://core-renderer-tiles.maps.yandex.net",

        ],

    }
}

# TALISMAN_DEV_CONFIG = {
#     "content_security_policy": {
#         "base-uri": ["'self'"],
#         "default-src": ["'self'"],
#         "img-src": [
#             "'self'",
#             "blob:",
#             "data:",
#             "https://*.maps.yandex.net",
#             "https://api-maps.yandex.ru",
#             "https://yandex.ru",
#         ],
#         "worker-src": ["'self'", "blob:"],
#         "child-src": ["'self'", "blob:", "https://api-maps.yandex.ru"],
#         "frame-src": ["'self'", "blob:", "https://api-maps.yandex.ru"],
#         "connect-src": [
#             "'self'",
#             "https://api.mapbox.com",
#             "https://events.mapbox.com",
#             "https://api-maps.yandex.ru",
#             "https://suggest-maps.yandex.ru",
#             "https://*.maps.yandex.net",
#             "https://yandex.ru",
#             "https://*.taxi.yandex.net",
#         ],
#         "object-src": "'none'",
#         "style-src": [
#             "'self'",
#             "blob:",
#             "'unsafe-inline'",
#         ],
#         "script-src": [
#             "'self'",
#             "https://api-maps.yandex.ru",
#             "https://suggest-maps.yandex.ru",
#             "http://*.maps.yandex.net",
#             "https://yandex.ru",
#             "https://yastatic.net",
#             "'unsafe-inline'",
#             "'unsafe-eval'",
#         ],
#     },
#     "content_security_policy_nonce_in": ["script-src"],
#     "force_https": False,
#     "session_cookie_secure": False,
# }
TALISMAN_ENABLED = False
# MAPBOX_API_KEY = "pk.eyJ1IjoicG9ka2hvbHl1emluYSIsImEiOiJjbTgzZG9rMHowcGhhMmlyNHh2azV0eG82In0.tJ2MI3Hqe5uR8c6iVFju2A"

