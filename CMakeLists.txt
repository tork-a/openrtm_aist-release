
get_cmake_property(_variableNames VARIABLES)
foreach (_variableName ${_variableNames})
  message(STATUS "${_variableName}=${${_variableName}}")
endforeach()

add_custom_target(compile_openrtm_aist ALL
  COMMAND ./build/autogen
  COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX}
  COMMAND make
  COMMAND env
  COMMAND make install DESTDIR=${PWD}/debian/ros-indigo-openrtm-aist
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})

install(FILES package.xml DESTINATION share/openrtm_aist/)
foreach(target rtm-config rtm-naming rtm-skelwrapper rtc-template coil-config rtcd rtcprof)
  install(CODE "execute_process(COMMAND cmake -E create_symlink ../../bin/${target} ${target} WORKING_DIRECTORY \${CMAKE_INSTALL_PREFIX}/share/openrtm_aist)")
endforeach()


