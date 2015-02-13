cmake_minimum_required(VERSION 2.8)

# Make sure libtool doesn't set RPATHs
# I REALLY wish there was a better way to do this...
execute_process(COMMAND bash -c "awk '/^include / { system(sprintf(\"cd /etc; cat %s 2>/dev/null\", \$2)); skip = 1; } { if (!skip) print \$0; skip = 0; }' < /etc/ld.so.conf | sed -e 's/#.*//;/^[   ]*hwcap[        ]/d;s/[:,      ]/ /g;s/=[^=]*$//;s/=[^= ]* / /g;s/\"//g;/^$/d' | tr '\n' ' '" OUTPUT_VARIABLE ld_so_conf_paths)
execute_process(COMMAND bash -c "echo $LD_LIBRARY_PATH | sed 's/:/ /g' | tr '\n' ' '" OUTPUT_VARIABLE ld_library_paths)
set(lt_cv_sys_lib_dlsearch_path_spec "/lib64 /usr/lib64 /lib /usr/lib ${ld_so_conf_paths}${ld_library_paths}${CMAKE_INSTALL_PREFIX}/lib")

# This target is straightforward: Use ./build/autogen to produce ./configure
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/configure
  COMMAND ${PROJECT_SOURCE_DIR}/build/autogen
  DEPENDS ${PROJECT_SOURCE_DIR}/build/autogen
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})

# Again, straightforward: Use ./configure to produce ./Makefile
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/Makefile
  COMMAND ${PROJECT_SOURCE_DIR}/configure --prefix=${CMAKE_INSTALL_PREFIX}
  DEPENDS ${PROJECT_SOURCE_DIR}/configure
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})

# Now we can invoke make, but only if the Makefile is present
add_custom_target(compile_openrtm_aist ALL
  DEPENDS ${PROJECT_SOURCE_DIR}/Makefile
  COMMAND export lt_cv_sys_lib_dlsearch_path_spec=${lt_cv_sys_lib_dlsearch_path_spec} && \$\(MAKE\) -C ${PROJECT_SOURCE_DIR})

# Install target depends on make target, but doesn't have ALL
add_custom_target(install_openrtm_aist
  DEPENDS compile_openrtm_aist
  COMMAND export lt_cv_sys_lib_dlsearch_path_spec=${lt_cv_sys_lib_dlsearch_path_spec} && \$\(MAKE\) -C ${PROJECT_SOURCE_DIR} install)

# This install CODE will trigger the target install_openrtm_aist
install(CODE "execute_process(COMMAND \"${CMAKE_COMMAND}\" --build \"${CMAKE_BINARY_DIR}\" --target install_openrtm_aist)")
install(FILES package.xml DESTINATION share/openrtm_aist/)
install(CODE "execute_process(COMMAND cmake -E make_directory \$ENV{DESTDIR}\${CMAKE_INSTALL_PREFIX}/lib/openrtm_aist/bin)")
foreach(target rtm-config rtm-naming rtm-skelwrapper rtc-template coil-config rtcd rtcprof)
  install(CODE "execute_process(COMMAND cmake -E create_symlink ../../../bin/${target} ${target} WORKING_DIRECTORY \$ENV{DESTDIR}\${CMAKE_INSTALL_PREFIX}/lib/openrtm_aist/bin)")
endforeach()
foreach(target SeqInComp SeqOutComp MyServiceConsumerComp MyServiceProviderComp)
  install(CODE "execute_process(COMMAND cmake -E create_symlink ../../../share/openrtm-1.1/example/${target} ${target} WORKING_DIRECTORY \$ENV{DESTDIR}\${CMAKE_INSTALL_PREFIX}/lib/openrtm_aist/bin)")
endforeach()

string(REGEX MATCH "catkin" need_catkin "$ENV{_}")
if(need_catkin)
  install(CODE "
## this is tricky force write catkin marker file
set(_catkin_marker_file \"\${CMAKE_INSTALL_PREFIX}/.catkin\")
# check if the develspace marker file exists yet
if(EXISTS \${_catkin_marker_file})
  file(READ \${_catkin_marker_file} _existing_sourcespaces)
  if(_existing_sourcespaces STREQUAL \"\")
    # write this sourcespace to the marker file
    file(WRITE \${_catkin_marker_file} \"${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}\")
  else()
    # append to existing list of sourcespaces if it's not in the list
    list(FIND _existing_sourcespaces \"${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}\" _existing_sourcespace_index)
    if(_existing_sourcespace_index EQUAL -1)
      file(APPEND \${_catkin_marker_file} \";${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}\")
    endif()
  endif()
else()
  # create a new develspace marker file
  # NOTE: extra care must be taken when running multiple catkin jobs in parallel
  #       so that this does not overwrite the result of a similar call in another package
  file(WRITE \${_catkin_marker_file} \"${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}\")
endif()
")
endif()

