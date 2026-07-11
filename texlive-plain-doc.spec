%global tl_name plain-doc
%global tl_revision 28424

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A list of plain.tex cs names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/plain-doc/csname.txt
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plain-doc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plain-doc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document constitutes a list of every control sequence name (csname)
described in the TeXbook, together with an indication of whether the
csname is a primitive TeX command, or is defined in plain.tex

