%define name    photon
%define Name    Photon
%define version 0.3.1
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Photon is a static HTML gallery generator
Source:         http://www.saillard.org/photon/%{Name}-%{version}.tar.bz2
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
%{_libdir}/python%{pyver}/site-packages/%{Name}
%{_datadir}/%{name}

