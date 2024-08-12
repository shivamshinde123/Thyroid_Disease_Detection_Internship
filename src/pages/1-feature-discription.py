
import streamlit as st


class FeatureDescription:

    def __init__(self) -> None:
        pass

    def featureDistription(self):
        st.header('Different Feature Discription')
        with st.expander('Thyroxine'):
            st.subheader('What is thyroxine?')
            st.caption("""Thyroxine is the main hormone secreted into the bloodstream by the thyroid gland. 
                        It is the inactive form and most of it is converted to an active form called triiodothyronine by organs such as the liver and kidneys. 
                        Thyroid hormones play vital roles in regulating the body’s metabolic rate, heart and digestive functions, muscle control, brain development and maintenance of bones.""")

            st.subheader('Alternative names for thyroxine')
            st.caption('T4; tetraiodothyronine; thyroxin')

            st.subheader('How is thyroxine controlled?')
            st.caption("""The production and release of thyroid hormones, thyroxine and triiodothyronine, is controlled by a feedback loop system that involves the hypothalamus in the brain and the pituitary and thyroid glands. 
            The hypothalamus secretes thyrotropin-releasing hormone which, in turn, stimulates the pituitary gland to produce thyroid stimulating hormone. This hormone stimulates the production of the thyroid hormones, thyroxine and triiodothyronine, by the thyroid gland.  
            This hormone production system is regulated by a feedback loop so that when the levels of the thyroid hormones (thyroxine and triiodothyronine) increase, they prevent the release of both thyrotropin-releasing hormone and thyroid stimulating hormone. 
            This system allows the body to maintain a constant level of thyroid hormones in the body.""")

            st.subheader('What happens if I have too much thyroxine?')
            st.caption("""The release of too much thyroxine in the bloodstream is known as thyrotoxicosis. 
            This may be caused by overactivity of the thyroid gland (hyperthyroidism), as in Graves' disease, inflammation of the thyroid or a benign tumour. 
            Thyrotoxicosis can be recognised by a goitre, which is a swelling of the neck due to enlargement of the thyroid gland. Other symptoms of thyrotoxicosis include intolerance to heat, weight loss, increased appetite, increased bowel movements, irregular menstrual cycle, rapid or irregular heartbeat, palpitations, tiredness, irritability, tremor, hair thinning/loss and retraction of the eyelids resulting in a staring appearance.""")

            st.subheader('What happens if I have too little thyroxine?')
            st.caption("""Too little production of thyroxine by the thyroid gland is known as hypothyroidism. 
            It may be caused by autoimmune diseases, poor iodine intake or caused by the use of certain drugs. 
            Sometimes, the cause is unknown. Thyroid hormones are essential for physical and mental development so untreated hypothyroidism before birth or during childhood can cause mental impairment and reduced growth.  
            Hypothyroidism in adults causes reduced metabolism. It can result in symptoms such as fatigue, intolerance of cold temperatures, low heart rate, weight gain, reduced appetite, poor memory, depression, stiffness of the muscles and reduced fertility.""")

            
        with st.expander('Anti-thyroid medicines'):
            st.caption("""Antithyroid medications—sometimes written as anti-thyroid medications—are a common treatment for hyperthyroidism, particularly if you have an ongoing form of hyperthyroidism caused by Graves' disease or a goiter. 
            The goal of antithyroid medications is to prevent the thyroid from producing excess amounts of hormone.""")

        with st.expander('I131_treatment '):
            st.subheader('Radioactive iodine (I-131) Therapy for Thyroid Cancer')
            st.caption("""Surgery is the main treatment for many thyroid cancers. For papillary and follicular thyroid cancer, where there are only 1 or 2 enlarged lymph nodes, radioactive iodine (RAI) treatment is done after surgery. 
            This is to treat any remaining cancer cells.""")
        
        with st.expander('Hypothyroid'):
            st.caption("""Hypothyroidism (also called underactive thyroid, low thyroid or hypothyreosis) is a disorder of the endocrine system in which the thyroid gland does not produce enough thyroid hormone. It can cause a number of symptoms, such as poor ability to tolerate cold, a feeling of tiredness, constipation, slow heart rate, depression, and weight gain.Occasionally there may be swelling of the front part of the neck due to goiter.Untreated cases of hypothyroidism during pregnancy can lead to delays in growth and intellectual development in the baby or congenital iodine deficiency syndrome.  
            Worldwide, too little iodine in the diet is the most common cause of hypothyroidism.Hashimoto's thyroiditis is the most common cause of hypothyroidism in countries with sufficient dietary iodine.Less common causes include previous treatment with radioactive iodine, injury to the hypothalamus or the anterior pituitary gland, certain medications, a lack of a functioning thyroid at birth, or previous thyroid surgery.The diagnosis of hypothyroidism, when suspected, can be confirmed with blood tests measuring thyroid-stimulating hormone (TSH) and thyroxine levels.  
            Salt iodization has prevented hypothyroidism in many populations.Thyroid hormone replacement with levothyroxine treats hypothyroidism.Medical professionals adjust the dose according to symptoms and normalization of the thyroxine and TSH levels.Thyroid medication is safe in pregnancy.Although an adequate amount of dietary iodine is important, too much may worsen specific forms of hypothyroidism.
            Worldwide about one billion people are estimated to be iodine-deficient; however, it is unknown how often this results in hypothyroidism.""")

        with st.expander('hyperthyroid'):
            st.caption("""Hyperthyroidism is the condition that occurs due to excessive production of thyroid hormones by the thyroid gland. Thyrotoxicosis is the condition that occurs due to excessive thyroid hormone of any cause and therefore includes hyperthyroidism. Some, however, use the terms interchangeably. Signs and symptoms vary between people and may include irritability, muscle weakness, sleeping problems, a fast heartbeat, heat intolerance, diarrhea, enlargement of the thyroid, hand tremor, and weight loss. Symptoms are typically less severe in the elderly and during pregnancy. An uncommon complication is thyroid storm in which an event such as an infection results in worsening symptoms such as confusion and a high temperature and often results in death. The opposite is hypothyroidism, when the thyroid gland does not make enough thyroid hormone.    
            Graves' disease is the cause of about 50% to 80% of the cases of hyperthyroidism in the United States. Other causes include multinodular goiter, toxic adenoma, inflammation of the thyroid, eating too much iodine, and too much synthetic thyroid hormone. A less common cause is a pituitary adenoma. The diagnosis may be suspected based on signs and symptoms and then confirmed with blood tests. Typically blood tests show a low thyroid stimulating hormone (TSH) and raised T3 or T4. Radioiodine uptake by the thyroid, thyroid scan, and TSI antibodies may help determine the cause.  
            Treatment depends partly on the cause and severity of disease. There are three main treatment options: radioiodine therapy, medications, and thyroid surgery. Radioiodine therapy involves taking iodine-131 by mouth which is then concentrated in and destroys the thyroid over weeks to months. The resulting hypothyroidism is treated with synthetic thyroid hormone. Medications such as beta blockers may control the symptoms, and anti-thyroid medications such as methimazole may temporarily help people while other treatments are having an effect. Surgery to remove the thyroid is another option. This may be used in those with very large thyroids or when cancer is a concern.""")
                        
        with st.expander('hypopituitary'):
            st.caption("""Hypopituitarism is a rare disorder in which your pituitary gland either fails to produce one or more of its hormones or doesn't produce enough of them. In hypopituitarism, you have a short supply of one or more of these pituitary hormones.""")

        with st.expander('TSH (Thyroid-stimulating hormone) Test'):
            st.subheader('What is a TSH test?')
            st.caption("""TSH stands for thyroid stimulating hormone. A TSH test is a blood test that measures this hormone. TSH levels that are too high or too low may be a sign of a thyroid problem.
            The thyroid is a small, butterfly-shaped gland in the front of your neck. Your thyroid makes hormones that control how your body uses energy. Thyroid hormones affect nearly every organ in your body, including your heart. They help control your weight, body temperature, muscle strength, and even your mood. If you don't have enough thyroid hormones in your blood, many of your body functions slow down. If you have too much, many body functions speed up.  
            Your thyroid is controlled by a gland in your brain, called the pituitary gland. The pituitary gland makes thyroid stimulating hormone (TSH). TSH tells your thyroid how much thyroid hormone it needs to make.  
            If the thyroid hormone levels in your blood are too low, your pituitary gland makes larger amounts of TSH to tell your thyroid to work harder. If your thyroid hormone levels are too high, the pituitary gland makes little or no TSH. By measuring TSH levels in your blood, you can find out if your thyroid is making the right level of hormones.  
            Other names: thyrotropin test""")
            st.subheader('What is it used for?')
            st.caption("""A TSH test is used to find out how well your thyroid is working. It can tell if you have hyperthyroidism (too much thyroid hormone) or hypothyroidism (too little thyroid hormone) in your blood. But a TSH test can't show what is causing a thyroid problem.  
            If you take prescription thyroid hormone medicine because of hypothyroidism or because you had your thyroid removed, you'll have regular TSH tests to check your thyroid hormone levels. TSH tests are also used to monitor your thyroid hormone levels after treatment for hyperthyroidism.""")
            st.subheader('Why do I need a TSH test?')
            st.caption("""You may need a TSH test if you have symptoms of too much or too little thyroid hormone in your blood.""")

        with st.expander('T3 (Triiodothyronine)'):
            st.caption('Triiodothyronine, or T3, is an important thyroid hormone that helps maintain muscle control, brain function and development, heart and digestive functions. A T3 blood test can help a doctor diagnose thyroid conditions. High or low T3 levels may indicate an overactive or underactive thyroid.')

        with st.expander('Total Thyroxine (T4) Test'):
            st.caption("""The total thyroxine test is used to diagnose thyroid disorders. Thyroxine (T4) is a thyroid hormone, and the test measures how much is in your blood. Some thyroid diseases are tied to too little T4, and others are tied to too much.  
Other names for this test are a total T4 test, total T4 concentration, and a thyroxine screen.""")
            
        with st.expander('T4U'):
            st.caption('T4U test is used by to dignore the thryroid disorder.')
        with st.expander('FTI'):
            st.caption('FTI test is used by to dignore the thryroid disorder.')


if __name__ == "__main__":
    fd = FeatureDescription()
    fd.featureDistription()
