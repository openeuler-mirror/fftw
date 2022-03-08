%bcond_with openmpi
%bcond_with mpich
%define debug_package %{nil}

%if %{with mpich}
%global mpi_list %{?mpi_list} mpich
%endif
%if %{with openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif

Name:             fftw
Version:          3.3.8
Release:          10
Summary:          A C subroutine library for computing the discrete Fourier transform
License:          GPLv2+
URL:              http://www.fftw.org
Source0:          http://www.fftw.org/fftw-%{version}.tar.gz
BuildRequires:    gcc-gfortran autoconf automake libtool time perl-interpreter gcc_secure make

%global quad 0
# disable quad-precision compile tempoary
%ifarch x86_64
%global quad 0
%endif

%if %{with mpich}
BuildRequires:    mpich-devel nss-myhostname
%endif

%if %{with openmpi}
BuildRequires:    openmpi-devel
%endif

%if %{with mpich} || %{with openmpi}
BuildRequires:    environment-modules
%endif

Requires(post):   info
Requires(preun):  info

%description
This package is a C subroutine library for computing the discrete Fourier transform (DFT) in one or more dimensions, of arbitrary input size,
and of both real and complex data (as well as of even/odd data, i.e. the discrete cosine/sine transforms or DCT/DST).

%package          libs
Summary:          FFTW run-time library
Provides:         fftw3 = %{version}-%{release}
Obsoletes:        fftw-libs-threads < %{version}-%{release} fftw-libs-openmp < %{version}-%{release}

Requires:         %{name}-libs-single = %{version}-%{release} %{name}-libs-double = %{version}-%{release}
Requires:         %{name}-libs-long = %{version}-%{release}

%if %{quad}
Requires:         %{name}-libs-quad = %{version}-%{release}
%endif

%description      libs
This Package is a dummy package.

%package          devel
Summary:          Header files and libraries for development
Provides:         fftw3-devel = %{version}-%{release} %{name}-static = %{version}-%{release}
Provides:         fftw3-static = %{version}-%{release}
Obsoletes:        %{name}-static < %{version}-%{release}

Requires:         pkgconfig %{name} = %{version}-%{release} %{name}-libs = %{version}-%{release}

%description      devel
The fftw-devel package contains the static libraries, the header files and other development content.

%package          libs-double
Summary:          FFTW library, double precision

%description      libs-double
This package contains the FFTW library compiled in double precision.

%package          libs-single
Summary:          FFTW library, single precision

%description      libs-single
This package contains the FFTW library compiled in single precision.

%package          libs-long
Summary:          FFTW library, long double precision

%description      libs-long
This package contains the FFTW library compiled in long double
precision.

%if %{quad}
%package          libs-quad
Summary:          The FFTW library compiled in quadruple precision

%description      libs-quad
This package contains the FFTW library compiled in quadruple precision.
%endif

%if %{with mpich}
%package          mpich-libs
Summary:          FFTW MPICH run-time library
Provides:         fftw3-mpich = %{version}-%{release}

Requires:         %{name}-mpich-libs-single = %{version}-%{release} %{name}-mpich-libs-double = %{version}-%{release}
Requires:         %{name}-mpich-libs-long = %{version}-%{release}

%description      mpich-libs
This package contains the FFTW MPICH run-time library.

%package          mpich-devel
Summary:          Header files and libraries for the FFTW MPICH library
Provides:         fftw3-mpich-devel = %{version}-%{release} fftw3-mpich-static = %{version}-%{release}
Provides:         %{name}-mpich-static = %{version}-%{release}
Obsoletes:        %{name}-mpich-static < %{version}-%{release}

Requires:         mpich-devel pkgconfig %{name}-devel = %{version}-%{release} %{name}-mpich-libs = %{version}-%{release}

%description      mpich-devel
This package contains the header files and development libraries for MPICH.

%package          mpich-libs-double
Summary:          Double precision
Requires:         %{name}-libs-double = %{version}-%{release}

%description      mpich-libs-double
This package contains the FFTW MPICH library compiled in double precision.

%package          mpich-libs-single
Summary:          Single precision
Requires:         %{name}-libs-single = %{version}-%{release}

%description      mpich-libs-single
This package contains the FFTW MPICH library compiled in single precision.

%package          mpich-libs-long
Summary:          Long double precision
Requires:         %{name}-libs-long = %{version}-%{release}

%description      mpich-libs-long
This package contains the FFTW MPICH library compiled in long double precision.
%endif

%if %{with openmpi}
%package          openmpi-libs
Summary:          FFTW OpenMPI run-time library
Provides:         fftw3-openmpi = %{version}-%{release}

Requires:         %{name}-openmpi-libs-single = %{version}-%{release} %{name}-openmpi-libs-double = %{version}-%{release}
Requires:         %{name}-openmpi-libs-long = %{version}-%{release}

%description      openmpi-libs
This package contains the individual FFTW.

%package          openmpi-devel
Summary:          Header files and libraries for the FFTW OpenMPI library
Provides:         fftw3-openmpi-devel = %{version}-%{release} fftw3-openmpi-static = %{version}-%{release}
Provides:         %{name}-openmpi-static = %{version}-%{release}
Obsoletes:        %{name}-openmpi-static < %{version}-%{release}
Requires:         openmpi-devel pkgconfig %{name}-devel = %{version}-%{release}  %{name}-openmpi-libs = %{version}-%{release}

%description      openmpi-devel
This package contains the header files and libraries for the FFTW OpenMPI library.

%package          openmpi-libs-double
Summary:          Double precision
Requires:         %{name}-libs-double = %{version}-%{release}

%description      openmpi-libs-double
This package contains the FFTW OpenMPI library compiled in double precision.

%package          openmpi-libs-single
Summary:          Single precision
Requires:         %{name}-libs-single = %{version}-%{release}

%description      openmpi-libs-single
This package contains the FFTW OpenMPI library compiled in single precision.

%package          openmpi-libs-long
Summary:          Long double precision
Requires:         %{name}-libs-long = %{version}-%{release}

%description      openmpi-libs-long
This package contains the FFTW OpenMPI library compiled in long double precision.
%endif

%package          help
Summary:          Help documentation related to %{name}
BuildArch:        noarch
Provides:         %{name}-doc = %{version}-%{release}
Obsoletes:        %{name}-doc < %{version}-%{release}

%description      help
This package includes help documentation and manuals related to %{name}

%prep
%autosetup -p1

%build
%if %{with mpich} || %{with openmpi}
source /etc/profile.d/modules.sh
%endif
autoreconf -vfi
export F77=gfortran

function build_section()
{
    ln -s ../configure .
    %configure --enable-shared --disable-dependency-tracking --enable-threads --enable-openmp $1
    sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
    sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
    %make_build
}

function mpi_build_section()
{
    ln -s ../configure .
    export CC=mpicc
    %configure --enable-shared --disable-dependency-tracking --enable-threads --enable-openmp $1 --enable-mpi --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin --sbindir=%{_libdir}/$mpi/sbin --includedir=%{_includedir}/$mpi-%{_arch} --mandir=%{_libdir}/$mpi/share/man
    %make_build
}

mkdir single double long quad
%ifarch x86_64
    cd single
    siarch="--enable-single --enable-sse2 --enable-avx"
    build_section $siarch
    cd ../double
    diarch="--enable-double --enable-sse2 --enable-avx"
    build_section $diarch
%else
    cd single
    build_section --enable-single
    cd ../double
    build_section --enable-double
%endif

cd ../long
build_section --enable-long-double

%if %{quad}
    cd ../quad
    build_section --enable-quad-precision
%endif
cd ..

%if %{with mpich} || %{with openmpi}
for mpi in %{mpi_list}
do
        module load mpi/${mpi}-%{_arch}
    mkdir ${mpi}-single ${mpi}-double ${mpi}-long ${mpi}-quad
    %ifarch x86_64
        cd ${mpi}-single
        msiarch="--enable-single --enable-sse2 --enable-avx"
        mpi_build_section $msiarch
        cd ../${mpi}-double
        mdiarch="--enable-double --enable-sse2 --enable-avx"
        mpi_build_section $mdiarch
    %else
        cd ${mpi}-single
        mpi_build_section --enable-single
        cd ../${mpi}-double
        mpi_build_section --enable-double
    %endif

    cd ../${mpi}-long
    mpi_build_section --enable-long-double
    cd ..
    module unload mpi/${mpi}-%{_arch}
done
%endif

%install
function install_section()
{
    %make_install -C ${mpi}-$1
    find %{buildroot}%{_libdir}/${mpi}/lib -name libfftw\* -a \! -name \*_mpi.\* -delete
    rm -r %{buildroot}%{_libdir}/${mpi}/{bin,share}
}
%if %{with mpich} || %{with openmpi}
source /etc/profile.d/modules.sh
%endif

%make_install -C single
%make_install -C double
%make_install -C long

%if %{quad}
    %make_install -C quad
%endif

%global delete_la  find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%if %{with mpich} || %{with openmpi}
for mpi in %{mpi_list}
do
    module load mpi/${mpi}-%{_arch}
    install_section single
    install_section double
    install_section long
    module unload mpi/${mpi}-%{_arch}
done
%endif

rm -f %{buildroot}%{_infodir}/dir
%delete_la

find %{buildroot} -type f -name '*.so*' -exec strip '{}' ';'

%check
%if %{with mpich} || %{with openmpi}
source /etc/profile.d/modules.sh
%endif
mydir=`pwd`

export LD_LIBRARY_PATH=$mydir/single/.libs:$mydir/single/threads/.libs
make %{?_smp_mflags} -C single check
export LD_LIBRARY_PATH=$mydir/double/.libs:$mydir/double/threads/.libs
make %{?_smp_mflags} -C double check
export LD_LIBRARY_PATH=$mydir/long/.libs:$mydir/long/threads/.libs
make %{?_smp_mflags} -C long check

%if %{quad}
    export LD_LIBRARY_PATH=$mydir/quad/.libs:$mydir/quad/threads/.libs
    make %{?_smp_mflags} -C quad check
%endif

%if %{with mpich} || %{with openmpi}
for mpi in %{mpi_list}
do
    module load mpi/${mpi}-%{_arch}
    export LD_LIBRARY_PATH=$mydir/${mpi}-single/.libs:$mydir/single/threads/.libs
    make %{?_smp_mflags} -C ${mpi}-single/mpi check
    export LD_LIBRARY_PATH=$mydir/${mpi}-double/mpi check
    export LD_LIBRARY_PATH=$mydir/${mpi}-long/.libs:$mydir/long/threads/.libs
    make %{?_smp_mflags} -C ${mpi}-long/mpi check
    module unload mpi/${mpi}-%{_arch}
done
%endif

%post libs-single -p /sbin/ldconfig
%postun libs-single -p /sbin/ldconfig
%post libs-double -p /sbin/ldconfig
%postun libs-double -p /sbin/ldconfig
%post libs-long -p /sbin/ldconfig
%postun libs-long -p /sbin/ldconfig

%if %{quad}
%post libs-quad -p /sbin/ldconfig
%postun libs-quad -p /sbin/ldconfig
%endif

%post devel
/sbin/install-info --section="Math" %{_infodir}/%{name}.info.gz %{_infodir}/dir  2>/dev/null || :

%preun devel
if [ "$1" = 0 ]
then
  /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir 2>/dev/null || :
fi

%files
%{_bindir}/fftw*-wisdom*
%exclude /usr/lib/debug/usr/bin/fftw*-wisdom*

%files libs

%files libs-single
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3f.so.*
%{_libdir}/libfftw3f_threads.so.*
%{_libdir}/libfftw3f_omp.so.*

%files libs-double
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3.so.*
%{_libdir}/libfftw3_threads.so.*
%{_libdir}/libfftw3_omp.so.*

%files libs-long
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3l.so.*
%{_libdir}/libfftw3l_threads.so.*
%{_libdir}/libfftw3l_omp.so.*

%if %{quad}
%files libs-quad
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3q.so.*
%{_libdir}/libfftw3q_threads.so.*
%{_libdir}/libfftw3q_omp.so.*
%endif

%files devel
%doc doc/FAQ/fftw-faq.html/
%doc %{_infodir}/fftw3.info*
%{_includedir}/fftw3*
%{_libdir}/cmake/fftw3/*.cmake
%{_libdir}/pkgconfig/fftw3*.pc
%{_libdir}/libfftw3*.{so,a}

%files help
%doc doc/*.pdf doc/html/
%{_mandir}/man1/fftw*.1*

%if %{with mpich}
%files mpich-libs

%files mpich-libs-single
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/mpich/lib/libfftw3f_mpi.so.*

%files mpich-libs-double
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/mpich/lib/libfftw3_mpi.so.*

%files mpich-libs-long
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/mpich/lib/libfftw3l_mpi.so.*

%files mpich-devel
%doc doc/FAQ/fftw-faq.html/
%{_includedir}/mpich-%{_arch}
%{_libdir}/mpich/lib/cmake/fftw3/*.cmake
%{_libdir}/mpich/lib/pkgconfig/fftw3*.pc
%{_libdir}/mpich/lib/libfftw3*.{so,a}
%endif

%if %{with openmpi}
%files openmpi-libs

%files openmpi-libs-single
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/openmpi/lib/libfftw3f_mpi.so.*

%files openmpi-libs-double
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/openmpi/lib/libfftw3_mpi.so.*

%files openmpi-libs-long
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/openmpi/lib/libfftw3l_mpi.so.*

%files openmpi-devel
%doc doc/FAQ/fftw-faq.html/
%{_includedir}/openmpi-%{_arch}
%{_libdir}/openmpi/lib/cmake/fftw3/*.cmake
%{_libdir}/openmpi/lib/pkgconfig/fftw3*.pc
%{_libdir}/openmpi/lib/libfftw3*.{so,a}
%endif

%changelog
* Mon Mar 7 2022 liyanan <liyanan32@huawei.com> - 3.3.8-10
- Fix self build fail

* Fri Mar 4 2022 baizhonggui <baizhonggui@huawei.com> - 3.3.8-9
- Strip the symbol table

* Fri Jan 7 2022 baizhonggui <baizhonggui@huawei.com> - 3.3.8-8
- disable the unused debuginfo to fix build fail

* Tue May 26 2020 Captain Wei <captain.a.wei@gmail.com> - 3.3.8-7
- isable quad-precision compile tempoary

* Wed Jan 15 2020 zhangrui <zhangrui182@huawei.com> - 3.3.8-6
- fix selfbuild fail

* Thu Dec 19 2019 zhujunhao <zhujunhao5@huawei.com> - 3.3.8-5
- Modify for x86 build fail

* Wed Nov 27 2019 dongjian <dongjian13@huawei.com> - 3.3.8-4
- Package init

* Fri Nov 15 2019 dongjian <dongjian13@huawei.com> - 3.3.8-3
- Package init
