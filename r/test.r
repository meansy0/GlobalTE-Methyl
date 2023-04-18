pheatmap(data)
pheatmap(data, cluster_row = FALSE)
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# chr [1:100] "#4575B4" "#4979B6" "#4E7DB8" "#5282BB" "#5786BD" "#5C8BBF" "#608FC2" ...
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
# chr [1:10] "#3288BD" "#5FA2CB" "#8DBCDA" "#BAD7E9" "#E8F1F7" "#FAE9EB" "#F1BEC4" ...
pheatmap(data, color = colours)
#colours = colorRampPalette(c("#3288bd", "white", "#d53e4f"))(10)
data <- as.matrix(data[, 2:6]) # 将数据框的2-5列转换为数值矩阵
data <- read.csv("get_g4gra.csv", header = TRUE)
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 2:6]) # 将数据框的2-5列转换为数值矩阵
pheatmap(data, cluster_row = FALSE)
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# chr [1:100] "#4575B4" "#4979B6" "#4E7DB8" "#5282BB" "#5786BD" "#5C8BBF" "#608FC2" ...
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
# chr [1:10] "#3288BD" "#5FA2CB" "#8DBCDA" "#BAD7E9" "#E8F1F7" "#FAE9EB" "#F1BEC4" ...
pheatmap(data, color = colours)
#colours = colorRampPalette(c("#3288bd", "white", "#d53e4f"))(10)
library(pheatmap)
data <- read.csv("get_g4gra.csv", header=TRUE, row.names=1)
rownames(data) <- data[, 1] # 将第一列设为行名
library(pheatmap)
data <- read.csv("get_g4gra.csv", header=TRUE, row.names=1)
rownames(data) <- data[, 1] # 将第一列设为行名
data
data <- read.csv("get_g4gra.csv", header=TRUE, row.names=1)
data
data <- read.csv("get_g4gra.csv", header=TRUE, row.names=1)
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 2:6]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours)
pheatmap(data, color = colours,treeheight_row = 0)
pheatmap(data,
color = colours,
cluster_rows = FALSE,
cluster_cols = FALSE,
breaks = 10,
annotation_col = data[, 1])
pheatmap(data,
color = colours,
cluster_rows = FALSE,
cluster_cols = FALSE,
breaks = 10)
pheatmap(data, color = colours, cluster_rows = 0, cluster_cols = 0, breaks = 10)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE, breaks = 10)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours,treeheight_row = 0)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE, breaks = 10)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE)
library(pheatmap)
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 2:6]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours,treeheight_row = 0)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE)
library(pheatmap)
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 2:6]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours,treeheight_row = 0)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE)
library(pheatmap)
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 2:6]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours,treeheight_row = 0)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE)
library(pheatmap)
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 2:3]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours,treeheight_row = 0)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE)
library(pheatmap)
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 4:6]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours,treeheight_row = 0)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,flip = "x")
pheatmap(data, color = colours, treeheight_row = 0, , angle_col = 45)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,angle_col = 45)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,angle_col = 90)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,angle_col = 180)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,angle_col = 270)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,angle_col = 0)
library(pheatmap)
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 2:3]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,angle_col = 0)
library(pheatmap)
data <- read.csv("get_g4gra.csv")
data
rownames(data) <- data[, 1] # 将第一列设为行名
data <- as.matrix(data[, 4:6]) # 将数据框的2-5列转换为数值矩阵
#Default
colours = colorRampPalette(rev(RColorBrewer::brewer.pal(n = 7, name = "RdYlBu")))(100)
str(colours)
# 个性化修改
colours = colorRampPalette(c("navy", "white", "firebrick3"))(10)
str(colours)
pheatmap(data, color = colours, cluster_rows = FALSE, cluster_cols = FALSE,angle_col = 0)
data <- read.table("data.csv", header = TRUE, sep = ",")
library(ggplot2)
library(scales)
ggplot(data, aes(x = sample, y = te, fill = sample)) +
geom_bar(stat = "identity", position = "dodge") +
labs(title = "Comparison of transposon methylation levels",
x = "Transposon family", y = "Methylation level")
# 读取数据
data <- read.csv("get_infor_csv.csv", header = TRUE)
data# 进行配对t检验
ttest <- t.test(data$have_g4_active, data$null_g4_active, paired=TRUE)
# 输出检验结果
ttest
library(ggplot2)
# 把数据转化为长格式
data_long <- gather(data, key = "type", value = "count", 2:3)
png("have_null_g4_active.png",  width = 800, height = 600, bg = "white", res = 120)
ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Comparison of All_g4_active and All_null_g4_active", x = "Sample", y = "Count") +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
# 把数据转化为长格式
data_long <- gather(data, key = "type", value = "count", 2:3)
ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Comparison of All_g4_active and All_null_g4_active", x = "Sample", y = "Count") +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Comparison of All_g4_active and All_null_g4_active", x = "Sample", y = "Count") +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
data_long
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Comparison of All_g4_active and All_null_g4_active", x = "Sample", y = "Count") +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
p
# 读入数据
data <- read.csv("get_g4gra.csv", header = TRUE, sep = ",")
# 整理数据为长格式
data_long <- data %>%
pivot_longer(cols = 2:4, names_to = "type", values_to = "count")
kruskal.test(count ~ type, data = data_long)
ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the active of different g4 gratitude groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_3", "G4_gra_1", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
ggsave("test1.png", plot = p, width = 8, height = 8, dpi = 300)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the active of different g4 gratitude groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_3", "G4_gra_1", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
ggsave("test1.png", plot = p, width = 8, height = 8, dpi = 300)
png("test1.png", width = 8, height = 8, units = "in", res = 300)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the active of different g4 gratitude groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_3", "G4_gra_1", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
print(p)
dev.off()
png("test1.png", width = 8, height = 8, units = "in", res = 300)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with  different gradient G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_3", "G4_gra_1", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
# Compare the activity with and without G4 groups
print(p)
dev.off()
# 整理数据为长格式
data_long <- data %>%
pivot_longer(cols = 4:6, names_to = "type", values_to = "count")
kruskal.test(count ~ type, data = data_long)
png("test2.png", width = 8, height = 8, units = "in", res = 300)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with  different gradient G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_3", "G4_gra_1", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
# Compare the activity with and without G4 groups
print(p)
dev.off()
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with  different gradient G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_1", "G4_gra_2", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
# Compare the activity with and without G4 groups
print(p)
dev.off()
data_long <- data %>%
pivot_longer(cols = 4:6, names_to = "type", values_to = "count")
kruskal.test(count ~ type, data = data_long)
png("test2.png", width = 8, height = 8, units = "in", res = 300)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with  different gradient G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_1", "G4_gra_2", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
# Compare the activity with and without G4 groups
print(p)
dev.off()
data_long <- data %>%
pivot_longer(cols = 2:3, names_to = "type", values_to = "count")
kruskal.test(count ~ type, data = data_long)
png("test1.png", width = 8, height = 8, units = "in", res = 300)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with  different gradient G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_have", "G4_null")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
# Compare the activity with and without G4 groups
print(p)
dev.off()
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with and without G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_have", "G4_null")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
#
print(p)
dev.off()
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with and without G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_have", "G4_null")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 18, face = "bold"),
axis.text.x = element_text(size = 12),
axis.text.y = element_text(size = 12),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 12))
#
print(p)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with and without G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_have", "G4_null")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 18, face = "bold"),
axis.text.x = element_text(size = 14),
axis.text.y = element_text(size = 14),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 14))
#
print(p)
dev.off()
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity with and without G4 groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_have", "G4_null")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 20, face = "bold"),
axis.text.x = element_text(size = 16),
axis.text.y = element_text(size = 16),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 16))
#
print(p)
dev.off()
data_long <- data %>%
pivot_longer(cols = 4:6, names_to = "type", values_to = "count")
kruskal.test(count ~ type, data = data_long)
png("test2.png", width = 8, height = 8, units = "in", res = 300)
p<-ggplot(data_long, aes(x = type, y = count, fill = type)) +
geom_boxplot(alpha = 0.8, notch = TRUE, notchwidth = 0.6, outlier.size = 2) +
labs(title = "Compare the activity of different  G4 gradient groups", x = "Group", y = "Count") +
scale_x_discrete(labels = c("G4_gra_1", "G4_gra_2", "G4_gra_3")) +
theme_minimal() +
theme(plot.title = element_text(hjust = 0.5, size = 20, face = "bold"),
axis.text.x = element_text(size = 16),
axis.text.y = element_text(size = 16),
legend.title = element_blank(),
legend.position = "bottom",
legend.text = element_text(size = 16))
#
print(p)
dev.off()
# Read in data from CSV file
data <- read.csv("your_csv_file.csv", header = TRUE)
# Read in data from CSV file
df <- read.csv("get_infor_csv.csv", header = TRUE)
# Compute correlation coefficient
correlation <- cor(df$genomesize, df$te_total, method = "pearson")
# Read in data from CSV file
data <- read.csv("data.csv", header = TRUE)
# Compute correlation coefficient
correlation <- cor(df$genomesize, df$te_total, method = "pearson")
# Compute correlation coefficient
correlation <- cor(df$genomesize, df$te, method = "pearson")
# Read in data from CSV file
df <- read.csv("data.csv", header = TRUE)
# Compute correlation coefficient
correlation <- cor(df$genomesize, df$te, method = "pearson")
# Create scatterplot with regression line
ggplot(df, aes(x = genomesize, y = te_total)) +
geom_point() +
geom_smooth(method = "lm", se = FALSE) +
geom_abline(intercept = 0, slope = correlation, linetype = "dashed") +
labs(x = "Genome size", y = "TE count", title = "Correlation between genome size and TE count")
RIdeogram
data <- read.csv("get_famliy_active.csv", header = TRUE,sep=',')
library(tidyr)
data_long <- gather(data, key = "name", value = "count", 2:6)
library(ggplot2)
ggplot(data_long, aes(x = name, y = count, fill = name)) +
geom_violin(draw_quantiles = c(0.25, 0.5, 0.75),
adjust = 1.5,
trim = FALSE,
scale = "width",
alpha = 0.7) +
scale_fill_brewer(palette = "Dark2") +
labs(title = "Transposon active by famliy", x = "Famliy", y = "Counts") +
theme_minimal() +
theme(panel.grid.major = element_blank(),
panel.grid.minor = element_blank(),
panel.border = element_blank(),
axis.line = element_line(colour = "black"),
axis.text.x = element_text(angle = 45, hjust = 1),
strip.text = element_text(size = 12, face = "bold"),
legend.position = "none")
# 提取四个家族的数据
family_1 <- subset(data_long, name == "DNA.MuDR")$count
family_2 <- subset(data_long, name == "LTR.Copia")$count
family_3 <- subset(data_long, name == "LTR.Gypsy")$count
family_4 <- subset(data_long, name == "RC.Helitron")$count
family_5 <- subset(data_long, name == "LINE.L1")$count
# p=6.893e-12(**)
# 进行Kruskal-Wallis检验
kruskal.test(list(family_1, family_2, family_3, family_4,family_5))
# 加载dunn.test包
library(dunn.test)
# 进行Dunn检验
dunn.test(data_long$count, data_long$name, method = "bonferroni")
data <- read.csv("tefamliy.csv", header = TRUE,sep=',')
library(tidyr)
data_long <- gather(data, key = "name", value = "count", 2:5)
library(ggplot2)
ggplot(data_long, aes(x = name, y = count, fill = name)) +
geom_violin(draw_quantiles = c(0.25, 0.5, 0.75),
adjust = 1.5,
trim = FALSE,
scale = "width",
alpha = 0.7) +
scale_fill_brewer(palette = "Dark2") +
labs(title = "Transposon counts by famliy", x = "Famliy", y = "Counts") +
theme_minimal() +
theme(panel.grid.major = element_blank(),
panel.grid.minor = element_blank(),
panel.border = element_blank(),
axis.line = element_line(colour = "black"),
axis.text.x = element_text(angle = 45, hjust = 1),
strip.text = element_text(size = 12, face = "bold"),
legend.position = "none")
# 提取四个家族的数据
family_1 <- subset(data_long, name == "DNA.MuDR")$count
family_2 <- subset(data_long, name == "LTR.Copia")$count
family_3 <- subset(data_long, name == "LTR.Gypsy")$count
family_4 <- subset(data_long, name == "RC.Helitron")$count
# p=6.893e-12(**)
# 进行Kruskal-Wallis检验
kruskal.test(list(family_1, family_2, family_3, family_4))
