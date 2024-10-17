Name:		texlive-bubblesort
Version:	56070
Release:	2
Summary:	Bubble sorts a list
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bubblesort
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bubblesort.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bubblesort.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bubblesort.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package sorts a list of TeX items {item 1}...{item k} in
"increasing" order where "increasing" is determined by a
comparator macro. By default it sorts real numbers with the
usual meaning of "increasing" but some other examples are
discussed in the documentation. A second macro is included
which sorts one list and applies the same permutation to a
second list.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bubblesort
%{_texmfdistdir}/tex/latex/bubblesort
%doc %{_texmfdistdir}/doc/latex/bubblesort

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
