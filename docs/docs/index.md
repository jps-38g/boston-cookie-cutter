# Boston Cookie Cutter documentation!

## Description

First testing of version control workflows with cookie cutter DS framework

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `gsutil rsync` to recursively sync files in `data/` up to `gs://user-bucket-schorr-bc-edu-lsehd-datascience-buckets/data/`.
* `make sync_data_down` will use `gsutil rsync` to recursively sync files in `gs://user-bucket-schorr-bc-edu-lsehd-datascience-buckets/data/` to `data/`.


