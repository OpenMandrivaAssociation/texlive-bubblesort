%global tl_name bubblesort
%global tl_revision 56070

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Bubble sorts a list
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bubblesort
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bubblesort.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bubblesort.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bubblesort.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package sorts a list of TeX items {item 1}...{item k} in
"increasing" order where "increasing" is determined by a comparator
macro. By default it sorts real numbers with the usual meaning of
"increasing" but some other examples are discussed in the documentation.
A second macro is included which sorts one list and applies the same
permutation to a second list.

