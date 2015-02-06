%define name    photon
%define Name    Photon
%define version 0.4.6
%define release 9

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Static HTML gallery generator
Source:         http://www.saillard.org/programs_and_patches/photon/files/%{Name}-%{version}.tar.bz2
Url:            http://www.saillard.org/photon/
License:        GPL
Group:          Graphics
BuildRequires:  python-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Photon is a photo album with a clean design.
Features:
* static HTML pages (you can put all pages and images on a CD-ROM)
* slideshow (use javascript optional)
* can use gimp to resize picture
* navigation between the image can use the keyboard (use javascript optional)
* works in any browser (Mozilla, Netscape Navigator 4.x, Konqueror, Opera)
* Each image can have a comment (with HTML tags)
* Information about the image (if taken from a digital picture) can be draw
* thumbnail image size can be chosen by the user
* output images can be scalled down
* control the number of thumbnail in a page.

%prep
%setup -q -n %{Name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README BUGS
%{_bindir}/%{name}
%{python_sitelib}/%{Name}
%{python_sitelib}/Photon-%{version}-py%{py_ver}.egg-info
%{_datadir}/%{name}



%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0.4.6-8mdv2011.0
+ Revision: 598912
- rebuild for py2.7

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.4.6-6mdv2010.0
+ Revision: 440845
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.4.6-5mdv2009.1
+ Revision: 325803
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.4.6-4mdv2009.0
+ Revision: 258967
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4.6-3mdv2009.0
+ Revision: 246862
- rebuild

* Fri Feb 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.6-1mdv2008.1
+ Revision: 176735
- new version

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4.4-2mdv2008.1
+ Revision: 171035
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.4-1mdv2008.0
+ Revision: 56119
- new version
- import photon


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-4mdv2007.0
- clean buildroot before install
- spec cleanup

* Thu Nov 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.1-3mdk
- Fix BuildRequires : add python-devel
- %%mkrel 

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.3.1-2mdk
- Rebuild for new python

* Fri Nov 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3.1-1mdk 
- first mdk package, using a spec file stolen from Luc Saillard <luc@saillard.org>
