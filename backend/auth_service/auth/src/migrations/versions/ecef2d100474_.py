"""empty message

Revision ID: ecef2d100474
Revises: 6f4f3dfabb48
Create Date: 2023-10-24 10:45:29.448022

"""
from alembic import op
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = 'ecef2d100474'
down_revision = '6f4f3dfabb48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(text("""
    --################################## Создаём Роли ###########################################
INSERT INTO "content"."roles" ("name","public_name","number") VALUES
('super_admin','Super Administrator','1'),
('admin','Administrator','2'),
('admin_platform','Admin Platform','3'),
('admin_account','Admin Account','4'),
('admin_collection','Admin Collection','5'),
('owner_collection','Owner Collection','6'),
('moderator_wl','Moderator WL','7'),
('moderator_list','Moderator List','8'),
('moderator_store','Moderator Store','9'),
('moderator_factory','Moderator Factory','10'),
('moderator_delivery','Moderator Delivery','11'),
('moderator_opportunity','Moderator Opportunity','12'),
('validator','Validator','13'),
('user','User','14');

--################################## Создаём Права ###########################################
INSERT INTO "content"."permissions" ("name") VALUES
('create_admin_platform'),
('update_admin_platform'),
('delete_admin_platform'),

('create_admin_account'),
('create_admin_account_in'),
('update_admin_account'),
('update_admin_account_in'),
('delete_admin_account'),
('delete_admin_account_in'),

('create_admin_collection'),
('create_admin_collection_in'),
('update_admin_collection'),
('update_admin_collection_in'),
('delete_admin_collection'),
('delete_admin_collection_in'),

('create_owner_collection_in'),
('create_owner_collection'),
('update_owner_collection_in'),
('update_owner_collection'),
('delete_owner_collection_in'),
('delete_owner_collection'),

('create_moderator_wl_in'),
('create_moderator_wl'),
('update_moderator_wl_in'),
('update_moderator_wl'),
('delete_moderator_wl_in'),
('delete_moderator_wl'),

('create_moderator_list'),
('create_moderator_list_in'),
('update_moderator_list'),
('update_moderator_list_in'),
('delete_moderator_list'),
('delete_moderator_list_in'),

('create_moderator_store_in'),
('create_moderator_store'),
('update_moderator_store_in'),
('update_moderator_store'),
('delete_moderator_store_in'),
('delete_moderator_store'),

('create_moderator_factory'),
('create_moderator_factory_in'),
('update_moderator_factory'),
('update_moderator_factory_in'),
('delete_moderator_factory'),
('delete_moderator_factory_in'),

('create_moderator_delivery_in'),
('create_moderator_delivery'),
('update_moderator_delivery_in'),
('update_moderator_delivery'),
('delete_moderator_delivery_in'),
('delete_moderator_delivery'),

('create_moderator_opportunity'),
('create_moderator_opportunity_in'),
('update_moderator_opportunity'),
('update_moderator_opportunity_in'),
('delete_moderator_opportunity'),
('delete_moderator_opportunity_in'),

('create_validator'),
('create_validator_in'),
('update_validator'),
('update_validator_in'),
('delete_validator'),
('delete_validator_in'),

('create_user'),
('create_user_in'),
('update_user'),
('update_user_in'),
('delete_user'),
('delete_user_in'),

('get_personal');



--################################## Создаём связи Роли-Права ###########################################

INSERT INTO "content"."roles_permissions" ("id","role_number","permission_name") VALUES
(gen_random_uuid(),'5','create_moderator_wl_in'),
(gen_random_uuid(),'5','update_moderator_wl_in'),
(gen_random_uuid(),'5','delete_moderator_wl_in'),
(gen_random_uuid(),'5','create_moderator_list_in'),
(gen_random_uuid(),'5','update_moderator_list_in'),
(gen_random_uuid(),'5','delete_moderator_list_in'),
(gen_random_uuid(),'5','create_moderator_store_in'),
(gen_random_uuid(),'5','update_moderator_store_in'),
(gen_random_uuid(),'5','delete_moderator_store_in'),
(gen_random_uuid(),'5','create_moderator_factory_in'),
(gen_random_uuid(),'5','update_moderator_factory_in'),
(gen_random_uuid(),'5','delete_moderator_factory_in'),
(gen_random_uuid(),'5','create_moderator_delivery_in'),
(gen_random_uuid(),'5','update_moderator_delivery_in'),
(gen_random_uuid(),'5','delete_moderator_delivery_in'),
(gen_random_uuid(),'5','get_personal');

INSERT INTO "content"."roles_permissions" ("id","role_number","permission_name") VALUES
(gen_random_uuid(),'4','create_admin_collection_in'),
(gen_random_uuid(),'4','update_admin_collection_in'),
(gen_random_uuid(),'4','delete_admin_collection_in'),
(gen_random_uuid(),'4','create_moderator_list_in'),
(gen_random_uuid(),'4','update_moderator_list_in'),
(gen_random_uuid(),'4','delete_moderator_list_in'),
(gen_random_uuid(),'4','create_moderator_wl_in'),
(gen_random_uuid(),'4','update_moderator_wl_in'),
(gen_random_uuid(),'4','delete_moderator_wl_in'),
(gen_random_uuid(),'4','create_moderator_store_in'),
(gen_random_uuid(),'4','update_moderator_store_in'),
(gen_random_uuid(),'4','delete_moderator_store_in'),
(gen_random_uuid(),'4','create_moderator_factory_in'),
(gen_random_uuid(),'4','update_moderator_factory_in'),
(gen_random_uuid(),'4','delete_moderator_factory_in'),
(gen_random_uuid(),'4','create_moderator_delivery_in'),
(gen_random_uuid(),'4','update_moderator_delivery_in'),
(gen_random_uuid(),'4','delete_moderator_delivery_in'),
(gen_random_uuid(),'4','get_personal');

INSERT INTO "content"."roles_permissions" ("id","role_number","permission_name") VALUES
(gen_random_uuid(),'3','create_admin_account'),
(gen_random_uuid(),'3','update_admin_account'),
(gen_random_uuid(),'3','delete_admin_account'),
(gen_random_uuid(),'3','create_admin_collection'),
(gen_random_uuid(),'3','update_admin_collection'),
(gen_random_uuid(),'3','delete_admin_collection'),
(gen_random_uuid(),'3','create_moderator_wl'),
(gen_random_uuid(),'3','update_moderator_wl'),
(gen_random_uuid(),'3','delete_moderator_wl'),
(gen_random_uuid(),'3','create_moderator_list'),
(gen_random_uuid(),'3','update_moderator_list'),
(gen_random_uuid(),'3','delete_moderator_list'),
(gen_random_uuid(),'3','create_moderator_store'),
(gen_random_uuid(),'3','update_moderator_store'),
(gen_random_uuid(),'3','delete_moderator_store'),
(gen_random_uuid(),'3','create_moderator_factory'),
(gen_random_uuid(),'3','update_moderator_factory'),
(gen_random_uuid(),'3','delete_moderator_factory'),
(gen_random_uuid(),'3','create_moderator_delivery'),
(gen_random_uuid(),'3','update_moderator_delivery'),
(gen_random_uuid(),'3','delete_moderator_delivery'),
(gen_random_uuid(),'3','create_moderator_opportunity'),
(gen_random_uuid(),'3','update_moderator_opportunity'),
(gen_random_uuid(),'3','delete_moderator_opportunity'),
(gen_random_uuid(),'3','get_personal');

INSERT INTO "content"."roles_permissions" ("id","role_number","permission_name") VALUES
(gen_random_uuid(),'2','create_admin_platform'),
(gen_random_uuid(),'2','update_admin_platform'),
(gen_random_uuid(),'2','delete_admin_platform'),
(gen_random_uuid(),'2','create_admin_account'),
(gen_random_uuid(),'2','update_admin_account'),
(gen_random_uuid(),'2','delete_admin_account'),
(gen_random_uuid(),'2','create_admin_collection'),
(gen_random_uuid(),'2','update_admin_collection'),
(gen_random_uuid(),'2','delete_admin_collection'),
(gen_random_uuid(),'2','create_moderator_wl'),
(gen_random_uuid(),'2','update_moderator_wl'),
(gen_random_uuid(),'2','delete_moderator_wl'),
(gen_random_uuid(),'2','create_moderator_list'),
(gen_random_uuid(),'2','update_moderator_list'),
(gen_random_uuid(),'2','delete_moderator_list'),
(gen_random_uuid(),'2','create_moderator_store'),
(gen_random_uuid(),'2','update_moderator_store'),
(gen_random_uuid(),'2','delete_moderator_store'),
(gen_random_uuid(),'2','create_moderator_factory'),
(gen_random_uuid(),'2','update_moderator_factory'),
(gen_random_uuid(),'2','delete_moderator_factory'),
(gen_random_uuid(),'2','create_moderator_delivery'),
(gen_random_uuid(),'2','update_moderator_delivery'),
(gen_random_uuid(),'2','delete_moderator_delivery'),
(gen_random_uuid(),'2','create_moderator_opportunity'),
(gen_random_uuid(),'2','update_moderator_opportunity'),
(gen_random_uuid(),'2','delete_moderator_opportunity'),
(gen_random_uuid(),'2','create_user'),
(gen_random_uuid(),'2','update_user'),
(gen_random_uuid(),'2','delete_user'),
(gen_random_uuid(),'2','get_personal');


INSERT INTO "content"."roles_permissions" ("id","role_number","permission_name") VALUES
(gen_random_uuid(),'1','create_admin_platform'),
(gen_random_uuid(),'1','update_admin_platform'),
(gen_random_uuid(),'1','delete_admin_platform'),
(gen_random_uuid(),'1','create_admin_account'),
(gen_random_uuid(),'1','update_admin_account'),
(gen_random_uuid(),'1','delete_admin_account'),
(gen_random_uuid(),'1','create_admin_collection'),
(gen_random_uuid(),'1','update_admin_collection'),
(gen_random_uuid(),'1','delete_admin_collection'),
(gen_random_uuid(),'1','create_moderator_wl'),
(gen_random_uuid(),'1','update_moderator_wl'),
(gen_random_uuid(),'1','delete_moderator_wl'),
(gen_random_uuid(),'1','create_moderator_list'),
(gen_random_uuid(),'1','update_moderator_list'),
(gen_random_uuid(),'1','delete_moderator_list'),
(gen_random_uuid(),'1','create_moderator_store'),
(gen_random_uuid(),'1','update_moderator_store'),
(gen_random_uuid(),'1','delete_moderator_store'),
(gen_random_uuid(),'1','create_moderator_factory'),
(gen_random_uuid(),'1','update_moderator_factory'),
(gen_random_uuid(),'1','delete_moderator_factory'),
(gen_random_uuid(),'1','create_moderator_delivery'),
(gen_random_uuid(),'1','update_moderator_delivery'),
(gen_random_uuid(),'1','delete_moderator_delivery'),
(gen_random_uuid(),'1','create_moderator_opportunity'),
(gen_random_uuid(),'1','update_moderator_opportunity'),
(gen_random_uuid(),'1','delete_moderator_opportunity'),
(gen_random_uuid(),'1','create_validator'),
(gen_random_uuid(),'1','update_validator'),
(gen_random_uuid(),'1','delete_validator'),
(gen_random_uuid(),'1','create_user'),
(gen_random_uuid(),'1','update_user'),
(gen_random_uuid(),'1','delete_user'),
(gen_random_uuid(),'1','get_personal');
    """))

    # ### end Alembic commands ###


def downgrade():
    pass
# ### end Alembic commands ###
