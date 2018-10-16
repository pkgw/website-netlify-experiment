+++
date = 2017-02-20T00:00:00-04:00
title = "Find out What Version of casacore is Used in a CASA Release"
weight = 0 # all howtos have zero weight => alphabetical ordering
template = "howto.html"
+++

To be *really* sure, I think you need to compile and run this short program:

```C++
// getvers.cxx
#define _GLIBCXX_USE_CXX11_ABI 0
#include <iostream>
#include <string>

namespace casa {
  const std::string getVersion();
  const std::string getVersionCASA();
}

int main(int argc, char **argv)
{
  std::cout << casa::getVersion() << std::endl;
  std::cout << casa::getVersionCASA() << std::endl;
  return 0;
}
```

Compile with:

```sh
g++ -o getvers getvers.cxx -lcasa_casa -L$CASALIBDIR -Wl,-rpath,$CASALIBDIR
```

May need to symlink `libcasa_casa.so.X.Y.Z` to just `libcasa_casa.so` in
`$CASALIBDIR`.

For CASA 4.7.1, I get 2.1.0 as the value `of getVersionCASA()`, which is a
reasonable casacore version number.
