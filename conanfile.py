from conans import CMake, ConanFile, tools
import os

class SpirvheadersConan(ConanFile):
    name = "spirv-headers"
    version = "1.5.3"
    url = "https://github.com/wumo-conan/spirv-headers"
    homepage = "https://github.com/KhronosGroup/SPIRV-Headers"
    settings = "os", "compiler", "build_type", "arch"
    
    no_copy_source = True
    
    def source(self):
        sha256 = "36e0cbd9213109b41bd99134e81a7fc9ffcffced3f9e75ca9db0150da1ebd723"
        tools.get("{}/archive/{}.zip".format(self.homepage, self.version))

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["SPIRV_HEADERS_SKIP_EXAMPLES"] = True
        cmake.configure(source_dir=os.path.join(
            self.source_folder, f"SPIRV-Headers-{self.version}"))
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
    
    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

        tools.rmdir(os.path.join(self.package_folder, "lib"))
    
    def package_id(self):
        self.info.header_only()
