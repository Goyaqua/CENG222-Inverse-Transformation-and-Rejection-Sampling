# CENG222-Inverse-Transformation-and-Rejection-Sampling
This repository contains a simulation project that explores two different methods for generating random samples of a variable X with a given cumulative distribution function (CDF). The methods used are the Inverse Transformation and Rejection Sampling techniques. The project includes:

- Generation of 30,000 samples of X using both methods.
- Real-time tracking of the average and variance of X across iterations.
- Detailed analysis and comparison of the experimental results with theoretical values.
- Pre-implemented plots that visualize the results of the experiments, including the average and variance of X.
- This project demonstrates how these sampling techniques can be used to model distributions and assess the accuracy of theoretical values for random variables.

Figure 3: This graph shows the cumulative distribution of the random variable 𝑈 and 𝑋𝑎. 

Figure 2: This graph illustrates the probability density function of 𝑈 and 𝑋𝑎.
𝑈 is uniformly distributed between 0 and 1, while 𝑋𝑎 exhibits a linear relationship with 
𝑈, corresponding to the exponential distribution of 𝑋𝑎.

Figure 1: This graph shows how the values of 𝑋𝑎 change with 𝑈. Since 𝑈
ranges from 0 to 1, and 𝑋𝑎 values will always be greater than 𝑈.

Figure 5: This graph shows the experimental average values of 𝑋𝑎.The average stabilizes near 0.67, which is very close to the theoretical mean 𝑀 = 0.67.

Figure 4: This graph shows the experimental variance of 𝑋𝑎. The variance stabilizes near 0.055, which matches the theoretical variance.

Figure 15: This graph shows the cumulative distribution function of 𝑋𝑏, generated using a different method. The distribution follows an exponential shape.

Figure 16: This graph displays the probability distribution function of 𝑋𝑏. The graph is linear since the PDF is f(x)=2x.

Figure 17: This graph shows the experimental average values of 𝑋𝑏, which stabilize near 0.68, again close to the theoretical mean 𝑀 = 0.67, generated using a different method.

Figure 18: This graph shows the experimental variance of 𝑋𝑏, which stabilizes near 0.055, consistent with the theoretical variance. The variance of 𝑋𝑏 closely matches that of 𝑋𝑎.

