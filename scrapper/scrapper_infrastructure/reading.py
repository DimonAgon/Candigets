
from infrastructure.enums import *


READING_VARIANTS = {
    ReadingVariant.Text: {
        AdParticular.PROFESSION,
        AdParticular.NAME,
        AdParticular.LOCATION,
        AdParticular.AGE,
        AdParticular.SALARY,
        AdParticular.JOBS_EXPERIENCES,
        AdParticular.CV_FULLNESS,
        AdParticular.UPDATE,
        AdParticular.CONNECTION_STATUS
    },

    ReadingVariant.Text.UNARY_TEXT: {
        AdParticular.PROFESSION,
        AdParticular.NAME,
        AdParticular.LOCATION,
        AdParticular.AGE,
        AdParticular.SALARY,
        AdParticular.CV_FULLNESS,
        AdParticular.UPDATE,
        AdParticular.CONNECTION_STATUS
    },

    ReadingVariant.Text.PARALLEL_TEXT: {
        AdParticular.JOBS_EXPERIENCES
    },

    ReadingVariant.Path: {
        AdParticular.SOURCE,
        AdParticular.PICTURE
    },

    ReadingVariant.Path.HYPER_REFERENCE: {
        AdParticular.SOURCE,
    },

    ReadingVariant.Path.SOURCE: {
        AdParticular.PICTURE
    }
}