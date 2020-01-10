%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_version: %global python_version %(%{__python} -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

Name:           qpid-tools
Version:        0.10
Release:        3%{?dist}
Summary:        Management and diagnostic tools for Apache Qpid

Group:          Development/Python
License:        ASL 2.0
URL:            http://qpid.apache.org
Source0:        %{name}-%{version}.tar.gz
Patch0:         mrg.patch
Patch1:         bz693847.patch
# svn export -r<rev> http://svn.apache.org/repos/asf/qpid/trunk/qpid/tools qpid-tools-0.7.<rev>
# tar czf qpid-tools-0.7.<rev>.tar.gz qpid-tools-0.7.<rev>
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel

Requires:       python-qpid >= 0.10
Requires:       python-qpid-qmf >= 0.10

%description
Management and diagnostic tools for Apache Qpid brokers and clients.

%prep
%setup -q
%patch0 -p3
%patch1 -p3

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/qpid-cluster
%{_bindir}/qpid-cluster-store
%{_bindir}/qpid-config
%{_bindir}/qpid-printevents
%{_bindir}/qpid-queue-stats
%{_bindir}/qpid-route
%{_bindir}/qpid-stat
%{_bindir}/qpid-tool
%{_bindir}/qmf-tool
%doc LICENSE.txt NOTICE.txt

%if "%{python_version}" >= "2.6"
%{python_sitelib}/qpid_tools-*.egg-info
%endif

%changelog
* Tue Apr 13 2011 Ted Ross <tross@redhat.com> - 0.10-3
- Related: rhbz#670956
- Fixed: Bug 670956 - qpid-tool does not support map arguments

* Tue Apr  5 2011 Justin Ross <jross@redhat.com> - 0.10-2
- Further fixes from upstream 0.10.

* Tue Mar 22 2011 Kenneth A. Giusti <kgiusti@redhat.com> - 0.10-1
- Related: bz679803.

* Wed Mar  9 2011 Kenneth A. Giusti <kgiusti@redhat.com> - 0.9.1078967-1
- Related: bz679803.

* Wed Feb 23 2011 Kenneth A. Giusti <kgiusti@redhat.com> - 0.9.1073306-1
- Resolves: bz679803.

* Fri Feb  4 2011 Kenneth A. Giusti <kgiusti@redhat.com> - 0.7.946106-5
- Resolves: bz619353, bz632678

* Wed Jun 30 2010 Kenneth A. Giusti <kgiusti@redhat.com> - 0.7.946106-4
- Resolves: rhbz609693

* Fri May 21 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-3
- Related: rhbz574881
- rhbz594537 - require same version of python-qmf

* Wed May 19 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-2
- Patch to qpid-tool
- Related: rhbz574881

* Wed May 19 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-1
- Rebased to svn rev 946106
- Related: rhbz574881

* Mon Apr 19 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.934605-2
- Added qpid-cluster-store.

* Mon Apr 19 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.934605-1
- Rebased to svn rev 934605.

* Thu Apr  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.930108-1
- Rebased to svn rev 930108.

* Wed Mar  3 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-4
- Changed defines to globals and moved to top.
- Fixed typo in description.
- Removed unnecessary python Requires/BuildRequires.

* Tue Mar  2 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-3
- Added correct version to python-qpid dependency.

* Mon Mar  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-2
- Conditionalize egg-info based on python version.

* Mon Mar  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917557-1
- Initial build.
