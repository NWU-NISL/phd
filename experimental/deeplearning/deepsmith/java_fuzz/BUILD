load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@cec_exports_repo//tools/bzl:exports_repo.bzl", "exports_repo")

py_binary(
    name = "encode_java_corpus",
    srcs = ["encode_java_corpus.py"],
    data = ["//deeplearning/clgen/corpuses/lexer:lexer_worker"],
    deps = [
        "//deeplearning/clgen/corpuses:encoded",
        "//deeplearning/clgen/corpuses:preprocessed",
        "//deeplearning/clgen/proto:clgen_pb_py",
        "//labm8/py:app",
        "//labm8/py:bazelutil",
        "//labm8/py:pbutil",
        "//labm8/py:sqlutil",
        "//third_party/py/numpy",
    ],
)

py_test(
    name = "encode_java_corpus_test",
    srcs = ["encode_java_corpus_test.py"],
    deps = [
        ":encode_java_corpus",
        "//deeplearning/clgen/corpuses:encoded",
        "//labm8/py:test",
        "//third_party/py/pytest",
    ],
)

py3_image(
    name = "encode_java_corpus_image",
    srcs = ["encode_java_corpus.py"],
    base = "@phd_base_java//image",
    main = "encode_java_corpus.py",
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [":encode_java_corpus"],
)

py_binary(
    name = "export_java_corpus",
    srcs = ["export_java_corpus.py"],
    deps = [
        "//datasets/github/scrape_repos:contentfiles",
        "//datasets/github/scrape_repos/preprocessors:extractors",
        "//labm8/py:app",
        "//labm8/py:fs",
        "//labm8/py:humanize",
        "//labm8/py:sqlutil",
    ],
)

py3_image(
    name = "export_java_corpus_image",
    srcs = ["export_java_corpus.py"],
    base = "@phd_base//image",
    main = "export_java_corpus.py",
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [":export_java_corpus"],
)

py_test(
    name = "export_java_corpus_test",
    srcs = ["export_java_corpus_test.py"],
    deps = [
        ":export_java_corpus",
        "//datasets/github/scrape_repos:contentfiles",
        "//labm8/py:test",
        "//third_party/py/pytest",
    ],
)

py_binary(
    name = "export_preprocessed_methods",
    srcs = ["export_preprocessed_methods.py"],
    deps = [
        "//deeplearning/clgen/corpuses:preprocessed",
        "//labm8/py:app",
        "//labm8/py:fs",
        "//third_party/py/progressbar",
    ],
)

py_binary(
    name = "export_rewriter_failures",
    srcs = ["export_rewriter_failures.py"],
    deps = [
        ":preprocess_java_corpus",
        "//datasets/github/scrape_repos:contentfiles",
        "//datasets/github/scrape_repos/proto:scrape_repos_pb_py",
        "//deeplearning/clgen/corpuses:preprocessed",
        "//deeplearning/clgen/preprocessors",
        "//labm8/py:app",
        "//labm8/py:fs",
        "//labm8/py:humanize",
        "//third_party/py/sqlalchemy",
    ],
)

py_binary(
    name = "mask_contentfiles",
    srcs = ["mask_contentfiles.py"],
    deps = [
        "//datasets/github/scrape_repos:contentfiles",
        "//labm8/py:app",
        "//labm8/py:humanize",
        "//third_party/py/sqlalchemy",
    ],
)

py3_image(
    name = "mask_contentfiles_image",
    srcs = ["mask_contentfiles.py"],
    base = "@phd_base//image",
    main = "mask_contentfiles.py",
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [":mask_contentfiles"],
)

py_binary(
    name = "scrape_java_files",
    srcs = ["scrape_java_files.py"],
    deps = [
        "//datasets/github:api",
        "//datasets/github/scrape_repos:contentfiles",
        "//datasets/github/scrape_repos:pipelined_scraper",
        "//datasets/github/scrape_repos/proto:scrape_repos_pb_py",
        "//labm8/py:app",
        "//third_party/py/github",
        "//third_party/py/progressbar",
        "//third_party/py/urllib3",
    ],
)

exports_repo(
    name = "export_github_fuzz_scraper",
    remote = "git@github.com:ChrisCummins/github_fuzz_scraper.git",
    tags = ["manual"],
    targets = [
        "//experimental/deeplearning/deepsmith/java_fuzz:scrape_java_files",
    ],
)

py3_image(
    name = "scrape_java_files_image",
    srcs = ["scrape_java_files.py"],
    base = "@phd_base//image",
    main = "scrape_java_files.py",
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [":scrape_java_files"],
)

py_binary(
    name = "preprocess_java_corpus",
    srcs = ["preprocess_java_corpus.py"],
    data = ["//deeplearning/clgen/preprocessors:JavaPreprocessor"],
    deps = [
        "//datasets/github/scrape_repos:contentfiles",
        "//datasets/github/scrape_repos/preprocessors:secrets",
        "//datasets/github/scrape_repos/proto:scrape_repos_pb_py",
        "//deeplearning/clgen/corpuses:preprocessed",
        "//deeplearning/clgen/proto:clgen_pb_py",
        "//labm8/py:app",
        "//labm8/py:bazelutil",
        "//labm8/py:fs",
        "//labm8/py:pbutil",
        "//third_party/py/sqlalchemy",
    ],
)

py3_image(
    name = "preprocess_java_corpus_image",
    srcs = ["preprocess_java_corpus.py"],
    base = "@phd_base_java//image",
    main = "preprocess_java_corpus.py",
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [":preprocess_java_corpus"],
)

py_test(
    name = "preprocess_java_corpus_test",
    srcs = ["preprocess_java_corpus_test.py"],
    deps = [
        ":preprocess_java_corpus",
        "//datasets/github/scrape_repos/proto:scrape_repos_pb_py",
        "//deeplearning/clgen/proto:clgen_pb_py",
        "//labm8/py:test",
    ],
)

py_binary(
    name = "gather_tensorboard_logs",
    srcs = ["gather_tensorboard_logs.py"],
    deps = [
        "//labm8/py:app",
        "//labm8/py:system",
        "//third_party/py/fs",
        "//third_party/py/tensorflow",
    ],
)

py_binary(
    name = "re_preprocess_java_methods",
    srcs = ["re_preprocess_java_methods.py"],
    deps = [
        ":preprocess_java_corpus",
        "//datasets/github/scrape_repos:contentfiles",
        "//datasets/github/scrape_repos/preprocessors:secrets",
        "//datasets/github/scrape_repos/proto:scrape_repos_pb_py",
        "//deeplearning/clgen/corpuses:preprocessed",
        "//deeplearning/clgen/proto:clgen_pb_py",
        "//labm8/py:app",
        "//labm8/py:bazelutil",
        "//labm8/py:pbutil",
    ],
)

py3_image(
    name = "re_preprocess_java_methods_image",
    srcs = ["re_preprocess_java_methods.py"],
    base = "@phd_base_java//image",
    main = "re_preprocess_java_methods.py",
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [":re_preprocess_java_methods"],
)

py_binary(
    name = "sample_java_model",
    srcs = ["sample_java_model.py"],
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [
        "//deeplearning/clgen",
        "//deeplearning/clgen:samples_database",
        "//deeplearning/clgen/corpuses:encoded",
        "//deeplearning/clgen/proto:clgen_pb_py",
        "//labm8/py:app",
        "//labm8/py:crypto",
        "//labm8/py:pbutil",
    ],
)

py_binary(
    name = "sample_opencl_model",
    srcs = ["sample_opencl_model.py"],
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [
        ":sample_java_model",
        "//deeplearning/clgen",
        "//deeplearning/clgen/proto:clgen_pb_py",
        "//labm8/py:app",
        "//research/cummins_2017_cgo:generative_model",
    ],
)

py3_image(
    name = "sample_java_model_image",
    srcs = ["sample_java_model.py"],
    base = "@phd_base_java//image",
    main = "sample_java_model.py",
    visibility = ["//experimental/deeplearning/deepsmith/java_fuzz:__subpackages__"],
    deps = [":sample_java_model"],
)

filegroup(
    name = "shared_code_README",
    srcs = ["shared_code_README.md"],
)
