/* THIS SAMPLE CODE IS PROVIDED AS IS        */
/* AND IS SUBJECT TO ALTERATIONS. GLYN       */
/* ACCEPTS NO RESPONSIBILITY OR LIABILITY    */
/* FOR ANY ERRORS OR                         */
/* ELIGIBILITY FOR ANY PURPOSES.             */
/* (C) GLYN GmbH & Co. KG                    */
/*********************************************
Project : copro_commands.h
          Graphic library
          EVE coprocessor commands
Version : 0.2 Status: Demo
Date    : 29.11.2013

Author  : P.Doerwald / GLYN GmbH & Co. KG

Releases: V0.2

Info    : O
*********************************************/

void cmd_clock(int x, int y, int r, U16 options, U16 h, U16 m, U16 s, U16 ms);
void cmd_gauge(int x, int y, int r, U16 options, U16 major, U16 minor, U16 val, U16 range);
void cmd_text(int x, int y, int font, int options, char* s);
void cmd_number(int x, int y, int font, int options, U32 n);
void cmd_track(int x, int y, int w, int h, int tag);
void cmd_bgcolor(U32 x);
void cmd_fgcolor(U32 x);
void cmd_button(int x,int y, int w, int h, int font, int options, char* s);
void cmd_dial(int x, int y, int r, U16 options, U16 val);
void cmd_keys(int x,int y, int w, int h, int font, int options, char* s);
void cmd_gradient(int x0, int y0, U32 rgb0, int x1, int y1, U32 rgb1);
void cmd_progress(int x, int y, int w, int h, U16 options, U16 val, U16 range);
void cmd_scrollbar(int x, int y, int w, int h, int options, int val, int size, int range);
void cmd_slider(int x, int y, int w, int h, U16 options, U16 val, U16 range);
void cmd_spinner(int x, int y, U16 style, U16 scale);
void cmd_coldstart(void);
void cmd_dlstart(void);
void cmd_stop(void);
void cmd_setfont(U32 font, U32 ptr);
void cmd_swap();
void cmd_logo(void);
void cmd_memzero(U32 ptr,U32 num);
void cmd_calibrate(void);
void cmd();
