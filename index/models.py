from  django.db import models
from  django.views.generic import ListView


class Articles(models.Model):
    site = models.ForeignKey('Sites', models.DO_NOTHING)
    clientid = models.ForeignKey('Clients', on_delete=models.CASCADE, db_column='clientid')
    insert_date = models.DateTimeField()
    article_date = models.DateTimeField()
    autor = models.CharField(max_length=128, blank=True, null=True)
    url = models.CharField(max_length=1022)
    article_name = models.TextField()
    article_text = models.TextField()
    visitors_count = models.IntegerField()
    is_top_artikle = models.IntegerField()
    screenshot_url = models.CharField(max_length=90, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    found_word = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'
        unique_together = (('id', 'site'), ('url', 'clientid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Notifications(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    sms = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Filterwords(models.Model):
    word = models.CharField(max_length=255, blank=True, null=True)
    wordalias = models.CharField(db_column='wordAlias', max_length=1022, blank=True, null=True)  # Field name made lowercase.
    subwordalias = models.CharField(max_length=255, blank=True, null=True)
    stopword = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(primary_key=True, auto_created=True)
    clientid = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'filterwords'


class Clients(models.Model):
    username = models.CharField(unique=True, max_length=255)
    tts_enabled = models.BooleanField()
    siteid = models.IntegerField(null=True, blank=True)
    notificationid = models.ForeignKey(Notifications, on_delete=models.CASCADE, db_column='notificationid', blank=True, null=True, unique=True)

    class Meta:
        managed = False
        db_table = 'clients'

    class ContactListView(ListView):
        paginate_by = 8


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sites(models.Model):
    id = models.IntegerField(primary_key=True)
    sitename = models.CharField(unique=True, max_length=128)
    internal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sites'


