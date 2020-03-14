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

run:
	@python $(SCRIPT_DIR)/run/run.py -c $(config_vars)

.PHONY: install-virtual-venv venv run db-migrate-generate db-migrate-up db-migrate-down
