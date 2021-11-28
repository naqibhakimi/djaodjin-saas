# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-12-13 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import saas.utils


class Migration(migrations.Migration):

    dependencies = [
        ("saas", "0005_role_extra"),
    ]

    operations = [
        migrations.CreateModel(
            name="UseCharge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=50, null=True)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("use_amount", models.PositiveIntegerField(default=0)),
                ("extra", models.TextField(null=True)),
            ],
            bases=(saas.utils.SlugTitleMixin, models.Model),
        ),
        migrations.RenameField(
            model_name="cartitem",
            old_name="nb_periods",
            new_name="quantity",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="email",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="sync_on",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="chargeitem",
            name="invoice_key",
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="chargeitem",
            name="sync_on",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="roledescription",
            name="skip_optin_on_grant",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="subscription",
            name="grant_key",
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name="subscription",
            name="request_key",
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="plan",
            field=models.ForeignKey(
                help_text="item added to the cart (if plan).",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="saas.Plan",
            ),
        ),
        migrations.AlterField(
            model_name="charge",
            name="state",
            field=models.PositiveSmallIntegerField(
                choices=[(3, "disputed"), (0, "created"), (2, "failed"), (1, "done")],
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="usecharge",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plans",
                to="saas.Plan",
            ),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="use",
            field=models.ForeignKey(
                help_text="item added to the cart (if use charge).",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="saas.UseCharge",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="usecharge",
            unique_together=set([("slug", "plan")]),
        ),
    ]
