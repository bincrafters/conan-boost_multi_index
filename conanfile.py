#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostMulti_IndexConan(base.BoostBaseConan):
    name = "boost_multi_index"
    url = "https://github.com/bincrafters/conan-boost_multi_index"
    lib_short_names = ["multi_index"]
    header_only_libs = ["multi_index"]
    b2_requires = [
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_foreach",
        "boost_integer",
        "boost_iterator",
        "boost_move",
        "boost_mpl",
        "boost_preprocessor",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits",
        "boost_utility"
    ]
