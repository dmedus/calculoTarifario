CREATE TABLE `calculo_tarifario`.`usuarios` (
`id` int (11) AUTO_INCREMENT,  
`usuario` varchar (150) DEFAULT NULL,  
`password` varchar (500) DEFAULT NULL,  
PRIMARY KEY (`id`)
);


INSERT INTO `calculo_tarifario`.`usuarios`
(`id`,
`usuario`,
`password`)
VALUES
(1,
'admin',
'admin');
