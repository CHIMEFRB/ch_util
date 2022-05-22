## v21.0.0 (2022-05-21)

### Fix

- **setup**: moved bitshuffle to chimefrb/bitshuffle fork, updated lock file
- **finder**: Rename StorageNode.mounted to StorageNode.active (#19)
- **finder**: Rename StorageNode.mounted to StorageNode.active
- **holography**: fix multi-user bug with create_from_ant_log
- **holography**: fix multi-user bug with create_from_ant_log
- **andata**: typos
- **layout**: remove broken layout ID support and linter errors
- **timing**: undefined and unraised exceptions and missing variable
- **layout**: remove identical redefinition and fix kw args
- **holography**: errors found by linter
- **ephemeris**: missing import
- **data_quality**: remove incorrect kw argument
- **subtract_rank1_signal**: wrong argument name
- **add_global_flags**: return None in the absence of anything better
- **hkpdata**: convert bytes to unicode in HKPData
- **cal_utils**: require a positive standard deviation (#38)
- remove PyEphem references
- **andata**: workaround for h5py/h5py#1750
- **cal_utils**: fixes bug in shape of Jacobian for polynomial models (#28)
- **layout**: Fix component.get_property (#34)

### Feat

- **ephemeris,tools**: refactor ephemeris and tools to use arbitrary caput.observer
- **tools**: added TONEAntenna objects for GBO outrigger
- **tools**: Change CHIME position
- **fluxcat,ephemeris**: add the specfind source catalog
- **holography**: make quality_flag a bitmask

### Refactor

- set minimum version to Python 3.6
- **timing**: improved timing correction

Features
========
- Capability to provide coeff_tau and coeff_alpha dataset. If provided, the timing correction for a particular sky input is a linear combination of the delay from each noise source input with the coefficients set by these [N_input, N_noise_source] arrays. If NOT provided, then the default behaviour is to use the map_input_to_noise_source method to map each sky input to the delay from a single noise source input (currently uses the noise source input on the same FPGA crate).

- Changes the algorithm used to determine the delay from the noise source data to more closely match what is done in the real-time pipeline. Specifically in regards to how outliers are identified and flagged, and how the spectral ripple in the noise source distribution system is removed.

- Capability to save results of eigen-decomposition to datasets in the timing correction object (useful for debugging).

- Adds weight_tau and weight_alpha datasets that contains the inverse variance on the delay (and amplitude) measurements from the noise source data. These uncertainties are propagated to uncertainties on the gain of the sky inputs.

Bug fixes
=========
- Cast inputs to float64 before passing to curve_fit. There is a bug in scipy < 1.3.0 where curve_fit will not optimize properly for mixed float32/float64 inputs (PR #10076 of scipy). This ensures that the dependent variable, independent variable, errors, and initial parameters in fit_poly_to_phase are float64. Previously curve_fit was not actually fitting the static phase versus frequency and was just returning the initial parameter estimates.

- Account for product conjugation when constructing the stacked timing correction. This corrects a bug that would have affected the application of the timing correction to stacked cross-polar data.
- **ephemeris**: use new functionality from caput
- **ephemeris**: remove `transit_RA` alias and raise exception if used

### BREAKING CHANGE

- this removes Python 2 support
- code still calling transit_RA will crash

# [20.10.0](https://github.com/chime-experiment/ch_util/compare/v20.5.0...v20.10.0) (2020-10-21)


### Bug Fixes

* **layout:** missing exception in layout db code ([b87de76](https://github.com/chime-experiment/ch_util/commit/b87de76bff058c7696c867bb0df4f3a9ebfd670a))
* **tools:** Set non-CHIME input delays to zero, not NaN. ([a20e5f6](https://github.com/chime-experiment/ch_util/commit/a20e5f6bdac631da3b33a944cbaa2a2c285bd873))


### Features

* **chimeweather:** add support for chime_weather files ([#22](https://github.com/chime-experiment/ch_util/issues/22)) ([04d400c](https://github.com/chime-experiment/ch_util/commit/04d400ce45ded6812283e765d125e4c6545c576d))
* **thermal:** Add amplitude thermal correction to cal_utils ([#25](https://github.com/chime-experiment/ch_util/issues/25)) ([ba36d37](https://github.com/chime-experiment/ch_util/commit/ba36d37294e32c8656eb1c9d44724a3e39b700b7))
* **tools:** add a property to CorrInput to track static delays ([38991ab](https://github.com/chime-experiment/ch_util/commit/38991ab1eb1a5351ebbffe8234535076bda209e8))
* **tools:** add delay calculation and decorrelation correction ([3c249e1](https://github.com/chime-experiment/ch_util/commit/3c249e1e19f84a6e2dc707920374911e4b937886))



# [20.5.0](https://github.com/chime-experiment/ch_util/compare/v0.3.0...v20.5.0) (2020-05-07)

Note: we have switched to calendar versioning for this release.

### Bug Fixes

* **andata.Corrdata.from_acq_h5_fast:** Skip missing datasets. ([7a36b64](https://github.com/chime-experiment/ch_util/commit/7a36b64db97a2a2ac184f6e5ceac95832d382cf6))
* **cal_utils:** cast inputs to float64 before passing to curve_fit. ([5462617](https://github.com/chime-experiment/ch_util/commit/5462617c04eac02afead99835aca6ddf8d325995)), closes [#10076](https://github.com/chime-experiment/ch_util/issues/10076)
* **cal_utils:** proper handling of abstract methods ([5f0e9ca](https://github.com/chime-experiment/ch_util/commit/5f0e9cab3bbaa8db4dfa595f74dbba96f6ccb5c2))
* **connectdb:** remove symbol deleted upstream ([4f063cf](https://github.com/chime-experiment/ch_util/commit/4f063cf0a06584075156036964a96f0df16ad3dc))
* **finder:** Fix imports. (pull request [#277](https://github.com/chime-experiment/ch_util/issues/277)) ([e74ea19](https://github.com/chime-experiment/ch_util/commit/e74ea19fb734c8d874f740417545e34af9915bc1))
* **fluxcat:** fixes bug in freq sort and issues in python 3 ([f8c3ca5](https://github.com/chime-experiment/ch_util/commit/f8c3ca548740e9cb3c78e7c4607421067002c7e5))
* **holography:** add import re to two functions which use it ([9c6fc8c](https://github.com/chime-experiment/ch_util/commit/9c6fc8c0cb7b3c538a1a691274c7dce782489c10))
* **holography:** fix print statement bug ([26c4d9e](https://github.com/chime-experiment/ch_util/commit/26c4d9eaaf0b01ac9fa5ad1eeaccad5150e12414))
* **pyproject.toml:** incorrectly quote dependency ([4baaf93](https://github.com/chime-experiment/ch_util/commit/4baaf934522c15b59e8c067bf12bfa4cb4937f26))
* **README:** update path to repository in the README ([8a8e7ec](https://github.com/chime-experiment/ch_util/commit/8a8e7ec14e6ecc54a00a2022066f994725bf0046))
* **setup.py:** missing requirement ([6b98a2c](https://github.com/chime-experiment/ch_util/commit/6b98a2c6c8a659e3a8c3bc9f6ade56c9be30e3d1))
* **timing:** Fix bug that crashed on unicode inputs strings. ([#14](https://github.com/chime-experiment/ch_util/issues/14)) ([f98f2ab](https://github.com/chime-experiment/ch_util/commit/f98f2abd9b8020ec17654b16f9acbb8ca2426989))
* **timing:** Robust check for gain dataset. ([a8dad3e](https://github.com/chime-experiment/ch_util/commit/a8dad3efae88cfdf41c04b035b79f3b4b9718166))
* remove symbols removed from chimedb.core ([6c0cea4](https://github.com/chime-experiment/ch_util/commit/6c0cea4b2e088b12dffc007c291e8ecd00e4b81e))
* use skyfield_wrapper to avoid re-downloading skyfield files ([af77d5e](https://github.com/chime-experiment/ch_util/commit/af77d5e80220a190b343aae36dfa686a0ccf873b))


### Features

* **andata:** add data classes for flaginput, gain, and digitalgain acquisitions. ([3026b25](https://github.com/chime-experiment/ch_util/commit/3026b25ee78e3a90da2dae86661c969a6db0907e)), closes [#289](https://github.com/chime-experiment/ch_util/issues/289)
* **andata:** improved conversion of index_maps and datasets to unicode ([41e5717](https://github.com/chime-experiment/ch_util/commit/41e571759b7ff22b17d0cc6a5ae2e0e4d2d42c89))
* **CorrData:** add `prodstack` property to CorrData ([0ff31f4](https://github.com/chime-experiment/ch_util/commit/0ff31f4a81262e70f9c8d2eb7659bc46760d6eb3))
* **CorrReader:** support reading when MPI distributed ([4f0891c](https://github.com/chime-experiment/ch_util/commit/4f0891cab154b286c2e06986023bd573485c6406))
* **ephemeris:** Add a catalog of pulsar holography sources to source_dictionary. ([2c8cb15](https://github.com/chime-experiment/ch_util/commit/2c8cb156bd8f7b8587e4c70a502513d7019f3bd9))
* **scripts:** Script for compiling a catalog of pulsar holography sources. ([af960ff](https://github.com/chime-experiment/ch_util/commit/af960ffd340864085a48fe23e85a3b69f0964409))
* **tools:** add method `redefine_stack_index_map` ([c9f672a](https://github.com/chime-experiment/ch_util/commit/c9f672aa7f3781f06599da06e54d3b01e4e285ef)), closes [#282](https://github.com/chime-experiment/ch_util/issues/282)
* **tools:** change the default CHIME rotation to -0.071 degrees ([25dd134](https://github.com/chime-experiment/ch_util/commit/25dd1345795a0879eac93f4c1a844e307458531a)), closes [#11](https://github.com/chime-experiment/ch_util/issues/11)
* **update_psrcat:** create pulsar catalog that can be used by FluxCatalog ([ff7011a](https://github.com/chime-experiment/ch_util/commit/ff7011a0a64b4c655ea7e2ec37aa61ed9ece09b2))
* **versioneer:** add versioneer for better version naming ([068efe8](https://github.com/chime-experiment/ch_util/commit/068efe8d5aed398161e2588f6ad6ef6a799b9458))
* peewee 3 support ([fb184a3](https://github.com/chime-experiment/ch_util/commit/fb184a3a2e540cf6256576af8b1e6f98dc6e8558))

