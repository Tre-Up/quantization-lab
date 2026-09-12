# Glossary

Plain-language definitions used in this repository.

## Parameter / weight
A learned number inside the model. A “27B model” has roughly 27 billion learned parameters. Quantization usually changes how those parameters are represented; it does **not** turn 27 billion parameters into 5 billion parameters.

## Precision
How many bits are used to represent a number and what number format is used.

## FP32 / FP16 / BF16
Floating-point formats. FP16 and BF16 use 16 bits per stored value and are common baselines for model weights.

## INT8 / INT4
Integer-style quantized representations using roughly 8 or 4 bits per quantized value, plus scales/metadata.

## Quantization
Representing model values with lower precision to reduce memory/storage and potentially improve inference efficiency.

## Post-training quantization (PTQ)
Quantizing an already trained model without retraining it from scratch.

## Quantization-aware training (QAT)
Training/fine-tuning while simulating or incorporating quantization behavior so the model adapts to it.

## Scale
A value used to map a range of original numbers into the smaller quantized number range and back.

## Zero-point
An offset used in some quantization schemes so the quantized integer range can represent a shifted real-value range.

## Symmetric quantization
Uses a range centered around zero, usually without a non-zero offset.

## Asymmetric quantization
Allows the represented range to be shifted using a zero-point.

## Group size
How many weights share quantization parameters such as a scale. Smaller groups can preserve accuracy better but add metadata/overhead.

## Outlier
A value or channel much larger/different than the majority. Outliers can make aggressive quantization difficult.

## Mixed precision / mixed bit-width
Different parts of the model use different precisions. Example: sensitive layers at 6 bits, tolerant layers at 3 bits.

## Calibration data
A small representative dataset used by some quantization methods to choose scales, importance, or other settings.

## Held-out evaluation
A test set not used to tune the method. It exists to test whether the final method generalizes.

## Weight compression ratio
Baseline weight bytes divided by quantized weight bytes.

## Peak runtime memory
The maximum memory observed while actually running a fixed inference workload.

## KV cache
Memory used to store attention keys/values for prior tokens during autoregressive generation. It grows with context and can become a major memory cost even after weights are quantized.

## Perplexity
A language-modeling metric related to how surprised the model is by text. Lower is generally better, but perplexity alone is not equivalent to downstream task quality.

## Quality retention
In this project, the quantized model's measured benchmark score relative to the original baseline score under a locked protocol.
