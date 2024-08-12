library(ggplot2)
library(ggrepel)

args = commandArgs(trailingOnly=TRUE)

# Plots the mean activity scores and meta pvalues from collected

cutoff = 0.05

multi_activity_stats <- read.table(args[1])
tfs = read.table(args[2])
colnames(multi_activity_stats) = c("mean_act", "pvals", "variance")
rownames(multi_activity_stats) = tfs$V1
multi_activity_stats$tfs = tfs$V1
multi_activity_stats$sign = multi_activity_stats$pvals < cutoff
multi_activity_stats$iter = seq(1,dim(multi_activity_stats)[1])

activity <- ggplot(multi_activity_stats,aes(iter,mean_act,col=factor(sign),size=variance))+geom_point()+scale_color_manual(values=c('grey','tomato'))+ theme_bw() + geom_label_repel(data=multi_activity_stats[which(multi_activity_stats$pvals<cutoff),], aes(label=tfs),size=2.0,col='black') + ggtitle(paste0("Individual sample mean activity scores. Metapval < ",as.character(cutoff)))
activity
ggsave(args[3])

