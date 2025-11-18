# Loading Fixtures Into a Fresh Database

1. Start with an empty database

Create a new empty database or clear an existing one:

```bash
python manage.py flush
```
If using a cloud database (Postgres/Neon/etc.), delete and recreate the DB instead of flushing.

2. Run migrations to create the schema

```bash
python manage.py migrate
```
Verify:
```bash
python manage.py dbshell
db=> \dt
```
You should see all project tables and no data.

3. Make sure Django signals do not auto-create related objects during fixture loading

Django calls Model.save(raw=True) when loading fixture rows.
Any post_save signal that auto-creates related objects must ignore raw=True, otherwise fixture loading produces duplicate OneToOne rows.

All signals should follow this pattern:

```python
@receiver(post_save, sender=MyModel)
def create_related_object(sender, instance, created, raw=False, **kwargs):
    if raw:
        return
    if created:
        RelatedModel.objects.create(my_model=instance)
```
Without this check, fixture loading will fail.

4. Load the fixture file

Once the database is empty, schema created, and signals safe:

```bash

python manage.py loaddata your_fixture_file.json
```
This inserts all rows in correct order without triggering unwanted side-effects.