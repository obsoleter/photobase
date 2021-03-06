# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Photo', fields ['height']
        db.create_index('photos_photo', ['height'])

        # Adding index on 'Photo', fields ['width']
        db.create_index('photos_photo', ['width'])

        # Adding index on 'Collection', fields ['name']
        db.create_index('photos_collection', ['name'])

        # Adding index on 'PublicCollection', fields ['published']
        db.create_index('photos_publiccollection', ['published'])


    def backwards(self, orm):
        # Removing index on 'PublicCollection', fields ['published']
        db.delete_index('photos_publiccollection', ['published'])

        # Removing index on 'Collection', fields ['name']
        db.delete_index('photos_collection', ['name'])

        # Removing index on 'Photo', fields ['width']
        db.delete_index('photos_photo', ['width'])

        # Removing index on 'Photo', fields ['height']
        db.delete_index('photos_photo', ['height'])


    models = {
        'photos.collection': {
            'Meta': {'object_name': 'Collection'},
            'cover_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"}),
            'cover_image_height': ('django.db.models.fields.IntegerField', [], {}),
            'cover_image_width': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_image_height': ('django.db.models.fields.IntegerField', [], {}),
            'member_image_width': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '300'}),
            'original': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        'photos.phototocollection': {
            'Meta': {'object_name': 'PhotoToCollection'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Collection']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"})
        },
        'photos.publiccollection': {
            'Meta': {'object_name': 'PublicCollection', '_ormbases': ['photos.Collection']},
            'collection_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['photos.Collection']", 'unique': 'True', 'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'})
        }
    }

    complete_apps = ['photos']