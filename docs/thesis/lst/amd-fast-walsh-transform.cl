kernel
void fastWalshTransform(global float * tArray,
                        const  int   step
                       )
{
    unsigned int tid = get_global_id(0);

    const unsigned int group = tid%step;
    const unsigned int pair  = 2*step*(tid/step) + group;

    const unsigned int match = pair + step;

    float T1          = tArray[pair];
    float T2          = tArray[match];

    tArray[pair]             = T1 + T2;
    tArray[match]            = T1 - T2;
}
