PROJECT_DIR=$(shell pwd)
SCRIPT_DIR=$(PROJECT_DIR)/scripts
DB_DIR=$(PROJECT_DIR)/simple_chat/db


# Override variables
# --------------------------------------------------------------------------------------------------
config_vars=dev


# Make commands
# --------------------------------------------------------------------------------------------------
install-virtual-venv:
	@python $(SCRIPT_DIR)/build/install-virtualenv.py

venv: install-virtual-venv
	@python $(SCRIPT_DIR)/build/setup_virtual_environment.py

db-migrate-generate:
	@python $(SCRIPT_DIR)/build/migrate_generate.py -c $(config_vars) -m $(message)

db-migrate-up:
	@python $(SCRIPT_DIR)/run/migrate_up.py -c $(config_vars)

db-migrate-down:
	@python $(SCRIPT_DIR)/run/migrate_down.py -c $(config_vars)

run:
	@python $(SCRIPT_DIR)/run/run.py -c $(config_vars)

.PHONY: install-virtual-venv venv run db-migrate-generate db-migrate-up db-migrate-down
