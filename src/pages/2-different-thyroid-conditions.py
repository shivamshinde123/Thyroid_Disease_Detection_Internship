
import streamlit as st


class DifferentThyroidConditions:

    def __init__(self) -> None:
        pass

    def diffConditions(self):
        # Metadata 2: Target Column Values Information
                st.header('Different Thyroid Conditions')
                st.markdown("""**Target metadata**  
                    The diagnosis consists of a string of letters indicating diagnosed conditions.
                    A diagnosis "Other" indicates no condition requiring comment.  A diagnosis of the
                    form "X|Y" is interpreted as "consistent with X, but more likely Y".  The
                    conditions are divided into groups where each group corresponds to a class of
                    comments.

                    Letter  Diagnosis
                    ------  ---------

                    hyperthyroid conditions:

                    A   hyperthyroid
                    B   T3 toxic
                    C   toxic goitre
                    D   secondary toxic

                    hypothyroid conditions:

                    E   hypothyroid
                    F   primary hypothyroid
                    G   compensated hypothyroid
                    H   secondary hypothyroid

                    binding protein:

                    I   increased binding protein
                    J   decreased binding protein

                    general health:

                    K   concurrent non-thyroidal illness

                    replacement therapy:

                    L   consistent with replacement therapy
                    M   underreplaced
                    N   overreplaced

                    antithyroid treatment:

                    O   antithyroid drugs
                    P   I131 treatment
                    Q   surgery

                    miscellaneous:

                    R   discordant assay results
                    S   elevated TBG
                    T   elevated thyroid hormones""")


if __name__ == "__main__":
    fd = DifferentThyroidConditions()
    fd.diffConditions()
