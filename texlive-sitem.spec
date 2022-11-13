Name:		texlive-sitem
Version:	22136
Release:	1
Summary:	Save the optional argument of \item
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sitem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sitem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sitem.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sitem.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package modifies \item commands to save the optional
argument in a box.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sitem/sitem.sty
%doc %{_texmfdistdir}/doc/latex/sitem/sitem.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sitem/sitem.dtx
%doc %{_texmfdistdir}/source/latex/sitem/sitem.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
