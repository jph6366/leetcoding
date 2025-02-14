#pragma once

#include <string.h>
#include <stdlib.h>

#define assert_eq(a, b) if (a != b) return EXIT_FAILURE
#define assert_diff(a, b) if (a == b) return EXIT_FAILURE
#define assert_gt(a, b) if (a <= b) return EXIT_FAILURE
#define assert_gte(a, b) if (a < b) return EXIT_FAILURE
#define assert_lt(a, b) if (a >= b) return EXIT_FAILURE
#define assert_lte(a, b) if (a > b) return EXIT_FAILURE

#define assert_str_eq(a, b) if (strcmp(a, b) != 0) return EXIT_FAILURE
#define assert_str_diff(a, b) if (strcmp(a, b) == 0) return EXIT_FAILURE

