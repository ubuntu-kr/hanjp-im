#ifndef __HANJP_AUTOMATA_H__
#define __HANJP_AUTOMATA_H__
#include <gmodule.h>

#define AM_RES_ERR -1
#define AM_RES_NOEVENT 0
#define AM_RES_COMMIT 1

enum output {
    HIRAGANA,
    KATAKANA
};

typedef struct HanjpAutomata HanjpAutomata;

HanjpAutomata* hanjp_automata_new(enum output init_type);
void hanjp_automata_set_output_type(HanjpAutomata* am, enum output type);
enum output hanjp_automata_get_output_type(HanjpAutomata* am);
const gunichar* hanjp_automata_get_string(HanjpAutomata* am);
gint hanjp_automata_push(gunichar c);
gunichar hanjp_automata_flush(HanjpAutomata* am);
void hanjp_automata_reset(HanjpAutomata* am);
void hanjp_automata_delete(HanjpAutomata* am);

#endif //__HANJP_AUTOMATA_H__