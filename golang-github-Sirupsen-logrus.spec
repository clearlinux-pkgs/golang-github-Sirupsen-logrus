#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-Sirupsen-logrus
Version  : 081307d9bc1364753142d5962fc1d795c742baaf
Release  : 1
URL      : https://github.com/Sirupsen/logrus/archive/081307d9bc1364753142d5962fc1d795c742baaf.tar.gz
Source0  : https://github.com/Sirupsen/logrus/archive/081307d9bc1364753142d5962fc1d795c742baaf.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-github-stretchr-testify

%description
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/Sirupsen/logrus.svg?branch=master)](https://travis-ci.org/Sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/Sirupsen/logrus?status.svg)](https://godoc.org/github.com/Sirupsen/logrus)

%prep
%setup -q -n logrus-081307d9bc1364753142d5962fc1d795c742baaf

%build

%install
gopath="/usr/lib/golang"
library_path=""
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/doc.go
/usr/lib/golang/src/entry.go
/usr/lib/golang/src/entry_test.go
/usr/lib/golang/src/examples/basic/basic.go
/usr/lib/golang/src/examples/hook/hook.go
/usr/lib/golang/src/exported.go
/usr/lib/golang/src/formatter.go
/usr/lib/golang/src/formatter_bench_test.go
/usr/lib/golang/src/formatters/logstash/logstash.go
/usr/lib/golang/src/formatters/logstash/logstash_test.go
/usr/lib/golang/src/hook_test.go
/usr/lib/golang/src/hooks.go
/usr/lib/golang/src/hooks/syslog/syslog.go
/usr/lib/golang/src/hooks/syslog/syslog_test.go
/usr/lib/golang/src/hooks/test/test.go
/usr/lib/golang/src/hooks/test/test_test.go
/usr/lib/golang/src/json_formatter.go
/usr/lib/golang/src/json_formatter_test.go
/usr/lib/golang/src/logger.go
/usr/lib/golang/src/logrus.go
/usr/lib/golang/src/logrus_test.go
/usr/lib/golang/src/terminal_bsd.go
/usr/lib/golang/src/terminal_linux.go
/usr/lib/golang/src/terminal_notwindows.go
/usr/lib/golang/src/terminal_solaris.go
/usr/lib/golang/src/terminal_windows.go
/usr/lib/golang/src/text_formatter.go
/usr/lib/golang/src/text_formatter_test.go
/usr/lib/golang/src/writer.go
