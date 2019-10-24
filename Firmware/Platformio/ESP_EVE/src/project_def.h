#ifndef _project_def_H_
#define _project_def_H_

#include "FT800Impl.h"
#include "FT800.h"
#include "FT_Transport_SPI.h"


//macros specific to FT800 hardware
/* Macros used for CS, PDN, INT pins for SPI - default values */
#define FT_CS_PIN 				10 
#define FT_PDN_PIN				8
#define FT_INT_PIN 				9
#define FT_DISPENABLE_PIN		7
#define FT_AUDIOENABLE_PIN		1

//macros related to arduino plaform SPI
/* SPI clock frequency */
#define FT_SPI_CLK_FREQ_MIN		8*1000000
#define FT_SPI_CLK_FREQ_MAX		21*1000000

/* Macros related to display dimensions */
#define FT_DISPLAYWIDTH		FT_DISPLAY_HSIZE_QVGA
#define FT_DISPLAYHEIGHT	FT_DISPLAY_VSIZE_QVGA
#define FT_DISPLAY_RESOLUTION	FT_DISPLAY_QVGA_320x240

/* Type definitions for class implementations */
typedef FT800Impl<FT_Transport_SPI> FT800IMPL_SPI;

#endif /* _project_def_ */
