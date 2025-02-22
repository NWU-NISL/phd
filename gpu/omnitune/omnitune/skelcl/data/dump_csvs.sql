.mode csv .header ON -------------------
-- ORACLE PARAMS --
-------------------
.out "oracle_params.csv"
SELECT scenarios.id AS scenario,
       width AS data_width,
       height AS data_height,
       tin AS data_tin,
       tout AS data_tout,
       north AS kern_north,
       south AS kern_south,
       east AS kern_east,
       west AS kern_west,
       instruction_count AS kern_instruction_count,
       ratio_ashr_insts AS kern_ratio_ashr_insts,
       ratio_add_insts AS kern_ratio_add_insts,
       ratio_alloca_insts AS kern_ratio_alloca_insts,
       ratio_and_insts AS kern_ratio_and_insts,
       ratio_br_insts AS kern_ratio_br_insts,
       ratio_call_insts AS kern_ratio_call_insts,
       ratio_fadd_insts AS kern_ratio_fadd_insts,
       ratio_fcmp_insts AS kern_ratio_fcmp_insts,
       ratio_fdiv_insts AS kern_ratio_fdiv_insts,
       ratio_fmul_insts AS kern_ratio_fmul_insts,
       ratio_fpext_insts AS kern_ratio_fpext_insts,
       ratio_fptosi_insts AS kern_ratio_fptosi_insts,
       ratio_fsub_insts AS kern_ratio_fsub_insts,
       ratio_getelementptr_insts AS kern_ratio_getelementptr_insts,
       ratio_icmp_insts AS kern_ratio_icmp_insts,
       ratio_insertvalue_insts AS kern_ratio_insertvalue_insts,
       ratio_load_insts AS kern_ratio_load_insts,
       ratio_mul_insts AS kern_ratio_mul_insts,
       ratio_or_insts AS kern_ratio_or_insts,
       ratio_phi_insts AS kern_ratio_phi_insts,
       ratio_ret_insts AS kern_ratio_ret_insts,
       ratio_sdiv_insts AS kern_ratio_sdiv_insts,
       ratio_sext_insts AS kern_ratio_sext_insts,
       ratio_sitofp_insts AS kern_ratio_sitofp_insts,
       ratio_srem_insts AS kern_ratio_srem_insts,
       ratio_select_insts AS kern_ratio_select_insts,
       ratio_shl_insts AS kern_ratio_shl_insts,
       ratio_store_insts AS kern_ratio_store_insts,
       ratio_sub_insts AS kern_ratio_sub_insts,
       ratio_trunc_insts AS kern_ratio_trunc_insts,
       ratio_udiv_insts AS kern_ratio_udiv_insts,
       ratio_xor_insts AS kern_ratio_xor_insts,
       ratio_zext_insts AS kern_ratio_zext_insts,
       ratio_basic_blocks AS kern_ratio_basic_blocks,
       ratio_memory_instructions AS kern_ratio_memory_instructions,
       ratio_non_external_functions AS kern_ratio_non_external_functions,
       max_wg_size AS kern_max_wg_size,
       COUNT AS dev_count,
                address_bits AS dev_address_bits,
                double_fp_config AS dev_double_fp_config,
                endian_little AS dev_endian_little,
                execution_capabilities AS dev_execution_capabilities,
                extensions AS dev_extensions,
                global_mem_cache_size AS dev_global_mem_cache_size,
                global_mem_cache_type AS dev_global_mem_cache_type,
                global_mem_cacheline_size AS dev_global_mem_cacheline_size,
                global_mem_size AS dev_global_mem_size,
                host_unified_memory AS dev_host_unified_memory,
                image2d_max_height AS dev_image2d_max_height,
                image2d_max_width AS dev_image2d_max_width,
                image3d_max_depth AS dev_image3d_max_depth,
                image3d_max_height AS dev_image3d_max_height,
                image3d_max_width AS dev_image3d_max_width,
                image_support AS dev_image_support,
                local_mem_size AS dev_local_mem_size,
                local_mem_type AS dev_local_mem_type,
                max_clock_frequency AS dev_max_clock_frequency,
                max_compute_units AS dev_max_compute_units,
                max_constant_args AS dev_max_constant_args,
                max_constant_buffer_size AS dev_max_constant_buffer_size,
                max_mem_alloc_size AS dev_max_mem_alloc_size,
                max_parameter_size AS dev_max_parameter_size,
                max_read_image_args AS dev_max_read_image_args,
                max_samplers AS dev_max_samplers,
                max_work_group_size AS dev_max_work_group_size,
                max_work_item_dimensions AS dev_max_work_item_dimensions,
                max_work_item_sizes_0 AS dev_max_work_item_sizes_0,
                max_work_item_sizes_1 AS dev_max_work_item_sizes_1,
                max_work_item_sizes_2 AS dev_max_work_item_sizes_2,
                max_write_image_args AS dev_max_write_image_args,
                mem_base_addr_align AS dev_mem_base_addr_align,
                min_data_type_align_size AS dev_min_data_type_align_size,
                native_vector_width_char AS dev_native_vector_width_char,
                native_vector_width_double AS dev_native_vector_width_double,
                native_vector_width_float AS dev_native_vector_width_float,
                native_vector_width_half AS dev_native_vector_width_half,
                native_vector_width_int AS dev_native_vector_width_int,
                native_vector_width_long AS dev_native_vector_width_long,
                native_vector_width_short AS dev_native_vector_width_short,
                preferred_vector_width_char AS dev_preferred_vector_width_char,
                preferred_vector_width_double AS dev_preferred_vector_width_double,
                preferred_vector_width_float AS dev_preferred_vector_width_float,
                preferred_vector_width_half AS dev_preferred_vector_width_half,
                preferred_vector_width_int AS dev_preferred_vector_width_int,
                preferred_vector_width_long AS dev_preferred_vector_width_long,
                preferred_vector_width_short AS dev_preferred_vector_width_short,
                queue_properties AS dev_queue_properties,
                single_fp_config AS dev_single_fp_config,
                TYPE AS dev_type,
                        vendor AS dev_vendor,
                        vendor_id AS dev_vendor_id,
                        VERSION AS dev_version,
                                   params AS wgsize
FROM oracle_params
LEFT JOIN scenarios ON oracle_params.scenario=scenarios.id
LEFT JOIN datasets ON scenarios.dataset=datasets.id
LEFT JOIN kernels ON scenarios.kernel=kernels.id
LEFT JOIN devices ON scenarios.device=devices.id;

-------------------
-- RUNTIME STATS --
-------------------
.out "runtime_stats.csv"
SELECT scenarios.id AS scenario,
       width AS data_width,
       height AS data_height,
       tin AS data_tin,
       tout AS data_tout,
       north AS kern_north,
       south AS kern_south,
       east AS kern_east,
       west AS kern_west,
       instruction_count AS kern_instruction_count,
       ratio_ashr_insts AS kern_ratio_ashr_insts,
       ratio_add_insts AS kern_ratio_add_insts,
       ratio_alloca_insts AS kern_ratio_alloca_insts,
       ratio_and_insts AS kern_ratio_and_insts,
       ratio_br_insts AS kern_ratio_br_insts,
       ratio_call_insts AS kern_ratio_call_insts,
       ratio_fadd_insts AS kern_ratio_fadd_insts,
       ratio_fcmp_insts AS kern_ratio_fcmp_insts,
       ratio_fdiv_insts AS kern_ratio_fdiv_insts,
       ratio_fmul_insts AS kern_ratio_fmul_insts,
       ratio_fpext_insts AS kern_ratio_fpext_insts,
       ratio_fptosi_insts AS kern_ratio_fptosi_insts,
       ratio_fsub_insts AS kern_ratio_fsub_insts,
       ratio_getelementptr_insts AS kern_ratio_getelementptr_insts,
       ratio_icmp_insts AS kern_ratio_icmp_insts,
       ratio_insertvalue_insts AS kern_ratio_insertvalue_insts,
       ratio_load_insts AS kern_ratio_load_insts,
       ratio_mul_insts AS kern_ratio_mul_insts,
       ratio_or_insts AS kern_ratio_or_insts,
       ratio_phi_insts AS kern_ratio_phi_insts,
       ratio_ret_insts AS kern_ratio_ret_insts,
       ratio_sdiv_insts AS kern_ratio_sdiv_insts,
       ratio_sext_insts AS kern_ratio_sext_insts,
       ratio_sitofp_insts AS kern_ratio_sitofp_insts,
       ratio_srem_insts AS kern_ratio_srem_insts,
       ratio_select_insts AS kern_ratio_select_insts,
       ratio_shl_insts AS kern_ratio_shl_insts,
       ratio_store_insts AS kern_ratio_store_insts,
       ratio_sub_insts AS kern_ratio_sub_insts,
       ratio_trunc_insts AS kern_ratio_trunc_insts,
       ratio_udiv_insts AS kern_ratio_udiv_insts,
       ratio_xor_insts AS kern_ratio_xor_insts,
       ratio_zext_insts AS kern_ratio_zext_insts,
       ratio_basic_blocks AS kern_ratio_basic_blocks,
       ratio_memory_instructions AS kern_ratio_memory_instructions,
       ratio_non_external_functions AS kern_ratio_non_external_functions,
       max_wg_size AS kern_max_wg_size, -- count                          as  dev_count,
 -- address_bits                   as  dev_address_bits,
 -- double_fp_config               as  dev_double_fp_config,
 -- endian_little                  as  dev_endian_little,
 -- execution_capabilities         as  dev_execution_capabilities,
 -- extensions                     as  dev_extensions,
 global_mem_cache_size AS dev_global_mem_cache_size,
 global_mem_cache_type AS dev_global_mem_cache_type,
 global_mem_cacheline_size AS dev_global_mem_cacheline_size,
 global_mem_size AS dev_global_mem_size,
 host_unified_memory AS dev_host_unified_memory, -- image2d_max_height             as  dev_image2d_max_height,
 -- image2d_max_width              as  dev_image2d_max_width,
 -- image3d_max_depth              as  dev_image3d_max_depth,
 -- image3d_max_height             as  dev_image3d_max_height,
 -- image3d_max_width              as  dev_image3d_max_width,
 -- image_support                  as  dev_image_support,
 local_mem_size AS dev_local_mem_size,
 local_mem_type AS dev_local_mem_type, -- max_clock_frequency            as  dev_max_clock_frequency,
 max_compute_units AS dev_max_compute_units, -- max_constant_args              as  dev_max_constant_args,
 -- max_constant_buffer_size       as  dev_max_constant_buffer_size,
 -- max_mem_alloc_size             as  dev_max_mem_alloc_size,
 -- max_parameter_size             as  dev_max_parameter_size,
 -- max_read_image_args            as  dev_max_read_image_args,
 -- max_samplers                   as  dev_max_samplers,
 -- max_work_group_size            as  dev_max_work_group_size,
 -- max_work_item_dimensions       as  dev_max_work_item_dimensions,
 -- max_work_item_sizes_0          as  dev_max_work_item_sizes_0,
 -- max_work_item_sizes_1          as  dev_max_work_item_sizes_1,
 -- max_work_item_sizes_2          as  dev_max_work_item_sizes_2,
 -- max_write_image_args           as  dev_max_write_image_args,
 -- mem_base_addr_align            as  dev_mem_base_addr_align,
 -- min_data_type_align_size       as  dev_min_data_type_align_size,
 -- native_vector_width_char       as  dev_native_vector_width_char,
 -- native_vector_width_double     as  dev_native_vector_width_double,
 -- native_vector_width_float      as  dev_native_vector_width_float,
 -- native_vector_width_half       as  dev_native_vector_width_half,
 -- native_vector_width_int        as  dev_native_vector_width_int,
 -- native_vector_width_long       as  dev_native_vector_width_long,
 -- native_vector_width_short      as  dev_native_vector_width_short,
 -- preferred_vector_width_char    as  dev_preferred_vector_width_char,
 -- preferred_vector_width_double  as  dev_preferred_vector_width_double,
 -- preferred_vector_width_float   as  dev_preferred_vector_width_float,
 -- preferred_vector_width_half    as  dev_preferred_vector_width_half,
 -- preferred_vector_width_int     as  dev_preferred_vector_width_int,
 -- preferred_vector_width_long    as  dev_preferred_vector_width_long,
 -- preferred_vector_width_short   as  dev_preferred_vector_width_short,
 -- queue_properties               as  dev_queue_properties,
 -- single_fp_config               as  dev_single_fp_config,
 TYPE AS dev_type,
         vendor AS dev_vendor, -- vendor_id                      as  dev_vendor_id,
 -- version                        as  dev_version,
 params.wg_c AS wg_c,
 params.wg_r AS wg_r,
 mean AS runtime
FROM runtime_stats
LEFT JOIN scenarios ON runtime_stats.scenario=scenarios.id
LEFT JOIN params ON runtime_stats.params=params.id
LEFT JOIN datasets ON scenarios.dataset=datasets.id
LEFT JOIN kernels ON scenarios.kernel=kernels.id
LEFT JOIN devices ON scenarios.device=devices.id
ORDER BY random()
LIMIT 50000;
