from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = "core"
    verbose_name = "Core"

    def ready(self):
        # import signals ở đây để register
        try:
            import core.signals  # noqa
        except Exception:
            pass
