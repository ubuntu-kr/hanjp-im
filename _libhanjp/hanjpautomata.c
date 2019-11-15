#include "hanjpautomata.h"
#include "hanjpchar.h"

//check batchim in state
enum state{
    //some states
};

struct HanjpAutomata{
    enum state state;
    enum consonant first;
    enum vowel secend;
    enum consonantState firstState;
    enum output output_type;
    gunichar string[4];
};

static gboolean hanjp_automata_commit(HanjpAutomata* am);
static gunichar hanjp_automata_flush_internal(HanjpAutomata* am);
