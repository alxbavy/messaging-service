from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from core.services.file_loader import FileLoaderService


class Command(BaseCommand):
    help = "Импортирует клиентов из Excel-файла"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        path = Path(options["file_path"])
        if not path.exists():
            raise CommandError(f"Файл не найден: {path}")

        stats = FileLoaderService().import_file(file_path=path)

        self.stdout.write(self.style.SUCCESS("Импорт завершён"))
        self.stdout.write(f"Создано клиентов: {stats.created}")
        self.stdout.write(f"Обновлено клиентов: {stats.updated}")
        self.stdout.write(f"Создано контактов: {stats.contacts_created}")
        self.stdout.write(f"Обновлено контактов: {stats.contacts_updated}")
        self.stdout.write(f"Пропущено строк: {stats.skipped}")

        if stats.errors:
            self.stdout.write(self.style.WARNING("Ошибки импорта:"))
            for error in stats.errors:
                self.stdout.write(f"- {error}")
