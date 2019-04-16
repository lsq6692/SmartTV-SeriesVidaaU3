# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cq.proto

# This file was originally generated by the protocol buffer compiler 2.6.1, but
# was subsequently manually edited to import protobuf26 instead of
# google.protobuf to prevent conflicts with a different version of
# google.protobuf that some users of depot_tools have installed. If you need
# to re-generate this file, please make similar changes again and add this
# comment back. More details on why we chose to rename the package can be
# found in the file depot_tools/third_party/protobuf26/README.chromium.

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from protobuf26 import descriptor as _descriptor
from protobuf26 import message as _message
from protobuf26 import reflection as _reflection
from protobuf26 import symbol_database as _symbol_database
from protobuf26 import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cq.proto',
  package='',
  serialized_pb=_b('\n\x08\x63q.proto\"\xef\x02\n\x06\x43onfig\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0f\n\x07\x63q_name\x18\x02 \x01(\t\x12\x1d\n\tverifiers\x18\x03 \x01(\x0b\x32\n.Verifiers\x12\x15\n\rcq_status_url\x18\x04 \x01(\t\x12%\n\x19hide_ref_in_committed_msg\x18\x05 \x01(\x08\x42\x02\x18\x01\x12\x1a\n\x12\x63ommit_burst_delay\x18\x06 \x01(\x05\x12\x18\n\x10max_commit_burst\x18\x07 \x01(\x05\x12\x15\n\rin_production\x18\x08 \x01(\x08\x12\x1b\n\x08rietveld\x18\t \x01(\x0b\x32\t.Rietveld\x12\x17\n\x06gerrit\x18\x0f \x01(\x0b\x32\x07.Gerrit\x12\x14\n\x0cgit_repo_url\x18\n \x01(\t\x12\x16\n\ntarget_ref\x18\x0b \x01(\tB\x02\x18\x01\x12\x18\n\x0csvn_repo_url\x18\x0c \x01(\tB\x02\x18\x01\x12\x1b\n\x13\x64raining_start_time\x18\r \x01(\t\".\n\x08Rietveld\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x15\n\rproject_bases\x18\x02 \x03(\t\"K\n\x06Gerrit\x12\x19\n\x11\x63q_verified_label\x18\x01 \x01(\t\x12&\n\x1e\x64ry_run_sets_cq_verified_label\x18\x02 \x01(\x08\"\xd5\t\n\tVerifiers\x12\x36\n\rreviewer_lgtm\x18\x01 \x01(\x0b\x32\x1f.Verifiers.ReviewerLgtmVerifier\x12=\n\x11gerrit_cq_ability\x18\x05 \x01(\x0b\x32\".Verifiers.GerritCQAbilityVerifier\x12\x36\n\x0btree_status\x18\x02 \x01(\x0b\x32!.Verifiers.TreeStatusLgtmVerifier\x12*\n\x07try_job\x18\x03 \x01(\x0b\x32\x19.Verifiers.TryJobVerifier\x12,\n\x08sign_cla\x18\x04 \x01(\x0b\x32\x1a.Verifiers.SignCLAVerifier\x1aw\n\x14ReviewerLgtmVerifier\x12\x16\n\x0e\x63ommitter_list\x18\x01 \x01(\t\x12\x15\n\rmax_wait_secs\x18\x02 \x01(\x05\x12\x13\n\x0bno_lgtm_msg\x18\x03 \x01(\t\x12\x1b\n\x13\x64ry_run_access_list\x18\x04 \x01(\t\x1as\n\x17GerritCQAbilityVerifier\x12\x16\n\x0e\x63ommitter_list\x18\x01 \x01(\t\x12\x1b\n\x13\x64ry_run_access_list\x18\x04 \x01(\t\x12#\n\x1b\x61llow_submit_with_open_deps\x18\x05 \x01(\x08\x1a\x31\n\x16TreeStatusLgtmVerifier\x12\x17\n\x0ftree_status_url\x18\x01 \x01(\t\x1a\x8a\x05\n\x0eTryJobVerifier\x12\x31\n\x07\x62uckets\x18\x01 \x03(\x0b\x32 .Verifiers.TryJobVerifier.Bucket\x12I\n\x14try_job_retry_config\x18\x02 \x01(\x0b\x32+.Verifiers.TryJobVerifier.TryJobRetryConfig\x1ag\n\x11\x45quivalentBuilder\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x0f\n\x07\x62uilder\x18\x02 \x01(\t\x12\x12\n\npercentage\x18\x03 \x01(\x05\x12\x1d\n\x15owner_whitelist_group\x18\x04 \x01(\t\x1a\x90\x01\n\x07\x42uilder\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0ctriggered_by\x18\x02 \x01(\t\x12\x1d\n\x15\x65xperiment_percentage\x18\x04 \x01(\x02\x12\x42\n\requivalent_to\x18\x05 \x01(\x0b\x32+.Verifiers.TryJobVerifier.EquivalentBuilder\x1aK\n\x06\x42ucket\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x08\x62uilders\x18\x02 \x03(\x0b\x32!.Verifiers.TryJobVerifier.Builder\x1a\xb0\x01\n\x11TryJobRetryConfig\x12\x1b\n\x13try_job_retry_quota\x18\x01 \x01(\x05\x12\x1a\n\x12global_retry_quota\x18\x02 \x01(\x05\x12\x1c\n\x14\x66\x61ilure_retry_weight\x18\x03 \x01(\x05\x12&\n\x1etransient_failure_retry_weight\x18\x04 \x01(\x05\x12\x1c\n\x14timeout_retry_weight\x18\x05 \x01(\x05\x1a\x11\n\x0fSignCLAVerifier')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Config.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cq_name', full_name='Config.cq_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verifiers', full_name='Config.verifiers', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cq_status_url', full_name='Config.cq_status_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hide_ref_in_committed_msg', full_name='Config.hide_ref_in_committed_msg', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='commit_burst_delay', full_name='Config.commit_burst_delay', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_commit_burst', full_name='Config.max_commit_burst', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_production', full_name='Config.in_production', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rietveld', full_name='Config.rietveld', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gerrit', full_name='Config.gerrit', index=9,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='git_repo_url', full_name='Config.git_repo_url', index=10,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_ref', full_name='Config.target_ref', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='svn_repo_url', full_name='Config.svn_repo_url', index=12,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='draining_start_time', full_name='Config.draining_start_time', index=13,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=380,
)


_RIETVELD = _descriptor.Descriptor(
  name='Rietveld',
  full_name='Rietveld',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='Rietveld.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project_bases', full_name='Rietveld.project_bases', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=428,
)


_GERRIT = _descriptor.Descriptor(
  name='Gerrit',
  full_name='Gerrit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cq_verified_label', full_name='Gerrit.cq_verified_label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dry_run_sets_cq_verified_label', full_name='Gerrit.dry_run_sets_cq_verified_label', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=430,
  serialized_end=505,
)


_VERIFIERS_REVIEWERLGTMVERIFIER = _descriptor.Descriptor(
  name='ReviewerLgtmVerifier',
  full_name='Verifiers.ReviewerLgtmVerifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='committer_list', full_name='Verifiers.ReviewerLgtmVerifier.committer_list', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_wait_secs', full_name='Verifiers.ReviewerLgtmVerifier.max_wait_secs', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_lgtm_msg', full_name='Verifiers.ReviewerLgtmVerifier.no_lgtm_msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dry_run_access_list', full_name='Verifiers.ReviewerLgtmVerifier.dry_run_access_list', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=786,
  serialized_end=905,
)

_VERIFIERS_GERRITCQABILITYVERIFIER = _descriptor.Descriptor(
  name='GerritCQAbilityVerifier',
  full_name='Verifiers.GerritCQAbilityVerifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='committer_list', full_name='Verifiers.GerritCQAbilityVerifier.committer_list', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dry_run_access_list', full_name='Verifiers.GerritCQAbilityVerifier.dry_run_access_list', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_submit_with_open_deps', full_name='Verifiers.GerritCQAbilityVerifier.allow_submit_with_open_deps', index=2,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=907,
  serialized_end=1022,
)

_VERIFIERS_TREESTATUSLGTMVERIFIER = _descriptor.Descriptor(
  name='TreeStatusLgtmVerifier',
  full_name='Verifiers.TreeStatusLgtmVerifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_status_url', full_name='Verifiers.TreeStatusLgtmVerifier.tree_status_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1024,
  serialized_end=1073,
)

_VERIFIERS_TRYJOBVERIFIER_EQUIVALENTBUILDER = _descriptor.Descriptor(
  name='EquivalentBuilder',
  full_name='Verifiers.TryJobVerifier.EquivalentBuilder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='Verifiers.TryJobVerifier.EquivalentBuilder.bucket', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='builder', full_name='Verifiers.TryJobVerifier.EquivalentBuilder.builder', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percentage', full_name='Verifiers.TryJobVerifier.EquivalentBuilder.percentage', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner_whitelist_group', full_name='Verifiers.TryJobVerifier.EquivalentBuilder.owner_whitelist_group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1220,
  serialized_end=1323,
)

_VERIFIERS_TRYJOBVERIFIER_BUILDER = _descriptor.Descriptor(
  name='Builder',
  full_name='Verifiers.TryJobVerifier.Builder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Verifiers.TryJobVerifier.Builder.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='triggered_by', full_name='Verifiers.TryJobVerifier.Builder.triggered_by', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiment_percentage', full_name='Verifiers.TryJobVerifier.Builder.experiment_percentage', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equivalent_to', full_name='Verifiers.TryJobVerifier.Builder.equivalent_to', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1326,
  serialized_end=1470,
)

_VERIFIERS_TRYJOBVERIFIER_BUCKET = _descriptor.Descriptor(
  name='Bucket',
  full_name='Verifiers.TryJobVerifier.Bucket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Verifiers.TryJobVerifier.Bucket.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='builders', full_name='Verifiers.TryJobVerifier.Bucket.builders', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1472,
  serialized_end=1547,
)

_VERIFIERS_TRYJOBVERIFIER_TRYJOBRETRYCONFIG = _descriptor.Descriptor(
  name='TryJobRetryConfig',
  full_name='Verifiers.TryJobVerifier.TryJobRetryConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='try_job_retry_quota', full_name='Verifiers.TryJobVerifier.TryJobRetryConfig.try_job_retry_quota', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='global_retry_quota', full_name='Verifiers.TryJobVerifier.TryJobRetryConfig.global_retry_quota', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failure_retry_weight', full_name='Verifiers.TryJobVerifier.TryJobRetryConfig.failure_retry_weight', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transient_failure_retry_weight', full_name='Verifiers.TryJobVerifier.TryJobRetryConfig.transient_failure_retry_weight', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout_retry_weight', full_name='Verifiers.TryJobVerifier.TryJobRetryConfig.timeout_retry_weight', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1550,
  serialized_end=1726,
)

_VERIFIERS_TRYJOBVERIFIER = _descriptor.Descriptor(
  name='TryJobVerifier',
  full_name='Verifiers.TryJobVerifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buckets', full_name='Verifiers.TryJobVerifier.buckets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='try_job_retry_config', full_name='Verifiers.TryJobVerifier.try_job_retry_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VERIFIERS_TRYJOBVERIFIER_EQUIVALENTBUILDER, _VERIFIERS_TRYJOBVERIFIER_BUILDER, _VERIFIERS_TRYJOBVERIFIER_BUCKET, _VERIFIERS_TRYJOBVERIFIER_TRYJOBRETRYCONFIG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1076,
  serialized_end=1726,
)

_VERIFIERS_SIGNCLAVERIFIER = _descriptor.Descriptor(
  name='SignCLAVerifier',
  full_name='Verifiers.SignCLAVerifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1728,
  serialized_end=1745,
)

_VERIFIERS = _descriptor.Descriptor(
  name='Verifiers',
  full_name='Verifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reviewer_lgtm', full_name='Verifiers.reviewer_lgtm', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gerrit_cq_ability', full_name='Verifiers.gerrit_cq_ability', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_status', full_name='Verifiers.tree_status', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='try_job', full_name='Verifiers.try_job', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sign_cla', full_name='Verifiers.sign_cla', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VERIFIERS_REVIEWERLGTMVERIFIER, _VERIFIERS_GERRITCQABILITYVERIFIER, _VERIFIERS_TREESTATUSLGTMVERIFIER, _VERIFIERS_TRYJOBVERIFIER, _VERIFIERS_SIGNCLAVERIFIER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=1745,
)

_CONFIG.fields_by_name['verifiers'].message_type = _VERIFIERS
_CONFIG.fields_by_name['rietveld'].message_type = _RIETVELD
_CONFIG.fields_by_name['gerrit'].message_type = _GERRIT
_VERIFIERS_REVIEWERLGTMVERIFIER.containing_type = _VERIFIERS
_VERIFIERS_GERRITCQABILITYVERIFIER.containing_type = _VERIFIERS
_VERIFIERS_TREESTATUSLGTMVERIFIER.containing_type = _VERIFIERS
_VERIFIERS_TRYJOBVERIFIER_EQUIVALENTBUILDER.containing_type = _VERIFIERS_TRYJOBVERIFIER
_VERIFIERS_TRYJOBVERIFIER_BUILDER.fields_by_name['equivalent_to'].message_type = _VERIFIERS_TRYJOBVERIFIER_EQUIVALENTBUILDER
_VERIFIERS_TRYJOBVERIFIER_BUILDER.containing_type = _VERIFIERS_TRYJOBVERIFIER
_VERIFIERS_TRYJOBVERIFIER_BUCKET.fields_by_name['builders'].message_type = _VERIFIERS_TRYJOBVERIFIER_BUILDER
_VERIFIERS_TRYJOBVERIFIER_BUCKET.containing_type = _VERIFIERS_TRYJOBVERIFIER
_VERIFIERS_TRYJOBVERIFIER_TRYJOBRETRYCONFIG.containing_type = _VERIFIERS_TRYJOBVERIFIER
_VERIFIERS_TRYJOBVERIFIER.fields_by_name['buckets'].message_type = _VERIFIERS_TRYJOBVERIFIER_BUCKET
_VERIFIERS_TRYJOBVERIFIER.fields_by_name['try_job_retry_config'].message_type = _VERIFIERS_TRYJOBVERIFIER_TRYJOBRETRYCONFIG
_VERIFIERS_TRYJOBVERIFIER.containing_type = _VERIFIERS
_VERIFIERS_SIGNCLAVERIFIER.containing_type = _VERIFIERS
_VERIFIERS.fields_by_name['reviewer_lgtm'].message_type = _VERIFIERS_REVIEWERLGTMVERIFIER
_VERIFIERS.fields_by_name['gerrit_cq_ability'].message_type = _VERIFIERS_GERRITCQABILITYVERIFIER
_VERIFIERS.fields_by_name['tree_status'].message_type = _VERIFIERS_TREESTATUSLGTMVERIFIER
_VERIFIERS.fields_by_name['try_job'].message_type = _VERIFIERS_TRYJOBVERIFIER
_VERIFIERS.fields_by_name['sign_cla'].message_type = _VERIFIERS_SIGNCLAVERIFIER
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Rietveld'] = _RIETVELD
DESCRIPTOR.message_types_by_name['Gerrit'] = _GERRIT
DESCRIPTOR.message_types_by_name['Verifiers'] = _VERIFIERS

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'cq_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  ))
_sym_db.RegisterMessage(Config)

Rietveld = _reflection.GeneratedProtocolMessageType('Rietveld', (_message.Message,), dict(
  DESCRIPTOR = _RIETVELD,
  __module__ = 'cq_pb2'
  # @@protoc_insertion_point(class_scope:Rietveld)
  ))
_sym_db.RegisterMessage(Rietveld)

Gerrit = _reflection.GeneratedProtocolMessageType('Gerrit', (_message.Message,), dict(
  DESCRIPTOR = _GERRIT,
  __module__ = 'cq_pb2'
  # @@protoc_insertion_point(class_scope:Gerrit)
  ))
_sym_db.RegisterMessage(Gerrit)

Verifiers = _reflection.GeneratedProtocolMessageType('Verifiers', (_message.Message,), dict(

  ReviewerLgtmVerifier = _reflection.GeneratedProtocolMessageType('ReviewerLgtmVerifier', (_message.Message,), dict(
    DESCRIPTOR = _VERIFIERS_REVIEWERLGTMVERIFIER,
    __module__ = 'cq_pb2'
    # @@protoc_insertion_point(class_scope:Verifiers.ReviewerLgtmVerifier)
    ))
  ,

  GerritCQAbilityVerifier = _reflection.GeneratedProtocolMessageType('GerritCQAbilityVerifier', (_message.Message,), dict(
    DESCRIPTOR = _VERIFIERS_GERRITCQABILITYVERIFIER,
    __module__ = 'cq_pb2'
    # @@protoc_insertion_point(class_scope:Verifiers.GerritCQAbilityVerifier)
    ))
  ,

  TreeStatusLgtmVerifier = _reflection.GeneratedProtocolMessageType('TreeStatusLgtmVerifier', (_message.Message,), dict(
    DESCRIPTOR = _VERIFIERS_TREESTATUSLGTMVERIFIER,
    __module__ = 'cq_pb2'
    # @@protoc_insertion_point(class_scope:Verifiers.TreeStatusLgtmVerifier)
    ))
  ,

  TryJobVerifier = _reflection.GeneratedProtocolMessageType('TryJobVerifier', (_message.Message,), dict(

    EquivalentBuilder = _reflection.GeneratedProtocolMessageType('EquivalentBuilder', (_message.Message,), dict(
      DESCRIPTOR = _VERIFIERS_TRYJOBVERIFIER_EQUIVALENTBUILDER,
      __module__ = 'cq_pb2'
      # @@protoc_insertion_point(class_scope:Verifiers.TryJobVerifier.EquivalentBuilder)
      ))
    ,

    Builder = _reflection.GeneratedProtocolMessageType('Builder', (_message.Message,), dict(
      DESCRIPTOR = _VERIFIERS_TRYJOBVERIFIER_BUILDER,
      __module__ = 'cq_pb2'
      # @@protoc_insertion_point(class_scope:Verifiers.TryJobVerifier.Builder)
      ))
    ,

    Bucket = _reflection.GeneratedProtocolMessageType('Bucket', (_message.Message,), dict(
      DESCRIPTOR = _VERIFIERS_TRYJOBVERIFIER_BUCKET,
      __module__ = 'cq_pb2'
      # @@protoc_insertion_point(class_scope:Verifiers.TryJobVerifier.Bucket)
      ))
    ,

    TryJobRetryConfig = _reflection.GeneratedProtocolMessageType('TryJobRetryConfig', (_message.Message,), dict(
      DESCRIPTOR = _VERIFIERS_TRYJOBVERIFIER_TRYJOBRETRYCONFIG,
      __module__ = 'cq_pb2'
      # @@protoc_insertion_point(class_scope:Verifiers.TryJobVerifier.TryJobRetryConfig)
      ))
    ,
    DESCRIPTOR = _VERIFIERS_TRYJOBVERIFIER,
    __module__ = 'cq_pb2'
    # @@protoc_insertion_point(class_scope:Verifiers.TryJobVerifier)
    ))
  ,

  SignCLAVerifier = _reflection.GeneratedProtocolMessageType('SignCLAVerifier', (_message.Message,), dict(
    DESCRIPTOR = _VERIFIERS_SIGNCLAVERIFIER,
    __module__ = 'cq_pb2'
    # @@protoc_insertion_point(class_scope:Verifiers.SignCLAVerifier)
    ))
  ,
  DESCRIPTOR = _VERIFIERS,
  __module__ = 'cq_pb2'
  # @@protoc_insertion_point(class_scope:Verifiers)
  ))
_sym_db.RegisterMessage(Verifiers)
_sym_db.RegisterMessage(Verifiers.ReviewerLgtmVerifier)
_sym_db.RegisterMessage(Verifiers.GerritCQAbilityVerifier)
_sym_db.RegisterMessage(Verifiers.TreeStatusLgtmVerifier)
_sym_db.RegisterMessage(Verifiers.TryJobVerifier)
_sym_db.RegisterMessage(Verifiers.TryJobVerifier.EquivalentBuilder)
_sym_db.RegisterMessage(Verifiers.TryJobVerifier.Builder)
_sym_db.RegisterMessage(Verifiers.TryJobVerifier.Bucket)
_sym_db.RegisterMessage(Verifiers.TryJobVerifier.TryJobRetryConfig)
_sym_db.RegisterMessage(Verifiers.SignCLAVerifier)


_CONFIG.fields_by_name['hide_ref_in_committed_msg'].has_options = True
_CONFIG.fields_by_name['hide_ref_in_committed_msg']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_CONFIG.fields_by_name['target_ref'].has_options = True
_CONFIG.fields_by_name['target_ref']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_CONFIG.fields_by_name['svn_repo_url'].has_options = True
_CONFIG.fields_by_name['svn_repo_url']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
