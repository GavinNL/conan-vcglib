#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class vcglibConan(ConanFile):
    name = "vcglib"
    version = "1.0.1"
    description = "Visualization and Computer Graphics Library"

    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "vcglib", "viz", "graphics")

    url = "https://github.com/gavinNL/conan-vcglib"
    homepage = "https://github.com/cnr-isti-vclab/vcglib"
    author = "GavinNL <>"
    license = "GPL"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    no_copy_source = True

    sha256 = "406e570637d3820810bf85fea7d8138ab8c70dfcb1be9941a0994ab3a793d1d0"

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    tar_file = "{0}/archive/v{1}.tar.gz".format(homepage, version)

    def source(self):
        source_url = "https://github.com/cnr-isti-vclab/vcglib"

        #tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256=self.sha256)
        tools.get(self.tar_file, sha256=self.sha256)

        extracted_dir = self.name + "-" + self.version
        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self._source_subfolder)


    def package(self):
        include_folder = os.path.join(self._source_subfolder, "")

        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)


    def package_id(self):
        self.info.header_only()
