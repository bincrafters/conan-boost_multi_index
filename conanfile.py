from conans import ConanFile, tools, os

class BoostMulti_IndexConan(ConanFile):
    name = "Boost.Multi_Index"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-multi_index"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["multi_index"]
    requires =  "Boost.Assert/1.65.1@bincrafters/testing", \
                      "Boost.Bind/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Detail/1.65.1@bincrafters/testing", \
                      "Boost.Foreach/1.65.1@bincrafters/testing", \
                      "Boost.Functional/1.65.1@bincrafters/testing", \
                      "Boost.Integer/1.65.1@bincrafters/testing", \
                      "Boost.Iterator/1.65.1@bincrafters/testing", \
                      "Boost.Move/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Preprocessor/1.65.1@bincrafters/testing", \
                      "Boost.Serialization/1.65.1@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
                      "Boost.Tuple/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing", \
                      "Boost.Utility/1.65.1@bincrafters/testing"

                      #assert1 bind3 config0 core2 detail5 foreach8 functional5 integer3 iterator5 move3 mpl5 preprocessor0 serialization11 smart_ptr4 static_assert1 throw_exception2 tuple4 type_traits3 utility5
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()