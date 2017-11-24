COMPANY_NAME ?= onlyoffice
PRODUCT_NAME ?= repo
PRODUCT_VERSION ?= 0.0.0
BUILD_NUMBER ?= 0

PACKAGE_NAME := $(COMPANY_NAME)-$(PRODUCT_NAME)
PACKAGE_VERSION := $(PRODUCT_VERSION)-$(BUILD_NUMBER)

RPM_ARCH = noarch

BUILD_DIR := $(PWD)/builddir
RPM := $(BUILD_DIR)/RPMS/$(RPM_ARCH)/$(PACKAGE_NAME)-$(PACKAGE_VERSION).$(RPM_ARCH).rpm

$(RPM):
	rpmbuild \
			-bb \
			--define "_topdir $(BUILD_DIR)" \
			--define "_package_name $(PACKAGE_NAME)" \
			--define "_product_version $(PRODUCT_VERSION)" \
			--define "_build_number $(BUILD_NUMBER)" \
			$(PACKAGE_NAME).spec

.PHONY: all clean install remove

all: $(RPM)

clean:
	rm -fr $(BUILD_DIR)

install:
	install onlyoffice.repo -t /etc/yum.repos.d

remove:
	rm /etc/yum.repos.d/onlyoffice.repo
