# revision 22136
# category Package
# catalog-ctan /macros/latex/contrib/sitem
# catalog-date 2011-04-19 10:29:51 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-sitem
Version:	1.0
Release:	1
Summary:	Save the optional argument of \item
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sitem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sitem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sitem.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sitem.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package modifies \item commands to save the optional
argument in a box.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sitem/sitem.sty
%doc %{_texmfdistdir}/doc/latex/sitem/sitem.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sitem/sitem.dtx
%doc %{_texmfdistdir}/source/latex/sitem/sitem.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
